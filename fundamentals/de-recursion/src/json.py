
def dumps(dictionary: dict):
    json_string = "{"
    for key, value in dictionary.items():
        if isinstance(key, tuple):
            continue
        json_string += f'"{key}": "{value}", '

    return json_string[:-2] + "}"
