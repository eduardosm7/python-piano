import json


def read_json(file):
    """
    Returns the a dict from the json

    :param file: Json file path
    :type file: str
    """
    json_file = open(file)
    json_str = json_file.read()
    return json.loads(json_str)    
