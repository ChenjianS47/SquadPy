import re


# Define a function for reading the map used in the server
def LogSquad_map(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: Success to Determine Startup Level : (.*) ",
                         data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Level = matchObj.group(2).split(" / ")[0]
    Layer = matchObj.group(2).split(" / ")[1]
    return (date, time, str(Level), str(Layer), server_id)
    pass

