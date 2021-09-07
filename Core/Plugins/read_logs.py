import codecs

# Define the function for read the logs
def read_logs(log_addrres, start_point):
    # Must use 'rb' for seek calculated by bytes
    fo = codecs.open(log_addrres, 'r', encoding='utf-8')
    # print("Filename: ", fo.name)
    # print("Updating the log file: ", fo.name)
    # Using the global variable，make start_point keeps in the newest position
    # Move the pointer to the newest position
    fo.seek(start_point, 1)
    line = fo.readlines()
    # Output the new postion of start_piont after reads the file
    start_point = fo.tell()
    fo.close()
    return line, start_point
    pass