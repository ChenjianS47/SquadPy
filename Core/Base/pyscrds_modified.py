# Copyright (C) 2013 Peter Rowlands
"""Source server RCON communications module"""

import struct
import socket
import itertools
import re

# Packet types
SERVERDATA_AUTH = 3
SERVERDATA_AUTH_RESPONSE = 2
SERVERDATA_EXECCOMMAND = 2
SERVERDATA_RESPONSE_VALUE = 0

# Special packet types for in-game chat in Squad
SERVERDATA_CHAT = 1


class RconPacket(object):
    """RCON packet"""

    def __init__(self, pkt_id=0, pkt_type=-1, body=''):
        self.pkt_id = pkt_id
        self.pkt_type = pkt_type
        self.body = body

    def __str__(self):
        """Return the body string."""
        return self.body

    def size(self):
        """Return the pkt_size field for this packet."""
        return len(self.body) + 10

    def pack(self):
        """Return the packed version of the packet."""
        return struct.pack('<3i{0}s'.format(len(self.body) + 2),
                           self.size(), self.pkt_id, self.pkt_type,
                           bytearray(self.body, 'utf-8'))


class RconConnection(object):
    """RCON client to server connection"""

    def __init__(self, server, port=27015, password='', single_packet_mode=False):
        """Construct an RconConnection.
        Parameters:
            server (str) server hostname or IP address
            port (int) server port number
            password (str) server RCON password
            single_packet_mode (bool) set to True for servers which do not hand 0-length SERVERDATA_RESPONSE_VALUE
                requests (i.e. Factorio).
        """
        self.server = server
        self.port = port
        self.single_packet_mode = single_packet_mode
        self._sock = socket.create_connection((server, port))
        self.pkt_id = itertools.count(1)
        self._authenticate(password)
        self.chat_message = 'NA'

    def _authenticate(self, password):
        """Authenticate with the server using the given password."""
        auth_pkt = RconPacket(next(self.pkt_id), SERVERDATA_AUTH, password)
        self._send_pkt(auth_pkt)
        # The server should respond with a SERVERDATA_RESPONSE_VALUE followed by SERVERDATA_AUTH_RESPONSE.
        # Note that some server types omit the initial SERVERDATA_RESPONSE_VALUE packet.
        auth_resp = self.read_response(auth_pkt)
        if auth_resp.pkt_type == SERVERDATA_RESPONSE_VALUE:
            auth_resp = self.read_response()
        if auth_resp.pkt_type != SERVERDATA_AUTH_RESPONSE:
            raise RconError('Received invalid auth response packet')
        if auth_resp.pkt_id == -1:
            raise RconAuthError('Bad password')

    def exec_command(self, command):
        """Execute the given RCON command.
        Parameters:
            command (str) the RCON command string (ex. "status")
        Returns the response body
        """
        cmd_pkt = RconPacket(next(self.pkt_id), SERVERDATA_EXECCOMMAND,
                             command)
        self._send_pkt(cmd_pkt)
        resp = self.read_response(cmd_pkt, True)
        return resp.body

    def _send_pkt(self, pkt):
        """Send one RCON packet over the connection.
            Raises:
                RconSizeError if the size of the specified packet is > 4096 bytes
        """
        if pkt.size() > 4096:
            raise RconSizeError('pkt_size > 4096 bytes')
        data = pkt.pack()
        self._sock.sendall(data)

    def _recv_pkt(self):
        """Read one RCON packet"""
        while True:
            header = self._sock.recv(struct.calcsize('<3i'))
            if len(header) != 0:
                break
        (pkt_size, pkt_id, pkt_type) = struct.unpack('<3i', header)
        # Change the variable body from bytes to str
        body = (self._sock.recv(pkt_size - 8)).decode('utf-8')
        return RconPacket(pkt_id, pkt_type, body)

    def read_response(self, request=None, multi=False):
        """Return the next response packet.
        Parameters:
            request (RconPacket) if request is provided, read_response() will check that the response ID matches the
                specified request ID
            multi (bool) set to True if read_response() should check for a multi packet response. If the current
                RconConnection has single_packet_mode enabled, this parameter is ignored.
        Raises:
            RconError if an error occurred while receiving the server response
        """
        if request and not isinstance(request, RconPacket):
            raise TypeError('Expected RconPacket type for request')
        if not self.single_packet_mode and multi:
            if not request:
                raise ValueError('Must specify a request packet in order to'
                                 ' read a multi-packet response')
            response = self._read_multi_response(request)
        else:
            response = self._recv_pkt()
        if not self.single_packet_mode and response.pkt_type not in (SERVERDATA_RESPONSE_VALUE, SERVERDATA_AUTH_RESPONSE):
            raise RconError('Recieved unexpected RCON packet type')
        if request and response.pkt_id != request.pkt_id:
            raise RconError('Response ID does not match request ID')
        return response

    def _read_multi_response(self, req_pkt):
        """Return concatenated multi-packet response."""
        chk_pkt = RconPacket(next(self.pkt_id), SERVERDATA_RESPONSE_VALUE)
        self._send_pkt(chk_pkt)
        # According to the Valve wiki, a server will mirror a
        # SERVERDATA_RESPONSE_VALUE packet and then send an additional response
        # packet with an empty body. So we should concatenate any packets until
        # we receive a response that matches the ID in chk_pkt
        body_parts = []
        while True:
            response = self._recv_pkt()
            if response.pkt_type != SERVERDATA_RESPONSE_VALUE:
                raise RconError('Received unexpected RCON packet type')
            if response.pkt_id == chk_pkt.pkt_id:
                break
            elif response.pkt_id != req_pkt.pkt_id:
                raise RconError('Response ID does not match request ID')
            body_parts.append(response.body)
        # Read and ignore the extra empty body response
        self._recv_pkt()
        return RconPacket(req_pkt.pkt_id, SERVERDATA_RESPONSE_VALUE,
                          ''.join(str(body_parts)))

    # Add this function for receive the in-game chat message
    def receive_chat_message(self):
        while True:
            header = self._sock.recv(struct.calcsize('<3i'))
            if len(header) != 0:
                break
        (pkt_size, pkt_id, pkt_type) = struct.unpack('<3i', header)
        if pkt_type == SERVERDATA_CHAT:
            chat_msg = ((self._sock.recv(pkt_size - 8)).decode('utf-8'))[:-2]
            pass
        else:
            chat_msg = ""
            pass
        # Delete the \x00\x00 at the end of the message
        if chat_msg != "":
            matchOjb = re.search(r'\[(.*)] \[SteamID:(.*)] (.*) : (.*)', chat_msg, re.M | re.I)
            chat_type = matchOjb.group(1)
            player_64id = matchOjb.group(2)
            player_name = matchOjb.group(3)
            chat_content = matchOjb.group(4)
            return chat_type, player_64id, player_name, chat_content
        pass


class RconError(Exception):
    """Generic RCON error."""
    pass


class RconAuthError(RconError):
    """Raised if an RCON Authentication error occurs."""
    pass




class RconSizeError(RconError):
    """Raised when an RCON packet is an illegal size."""
    pass
