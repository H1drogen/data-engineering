def flatten(list_to_flatten, depth = 1, depth_count = 0):
    new_list = []
    for entry in list_to_flatten:
        if isinstance(entry, list) and depth_count < depth:
            depth_count += 1
            new_list.extend(flatten(entry, depth, depth_count))
        else:
            new_list.append(entry)
    return new_list


def deep_entries(dictionary):
    output = ()
    for key, value in dictionary.items():
        if isinstance(value, dict):
            output += (key, deep_entries(value)),
        else:
            output += (key, value),
    return output
