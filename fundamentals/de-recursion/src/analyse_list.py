

# def analyse_list(word, items):
#     solution = {}
#     for index, item in enumerate(items):
#         temp = dict(f"{word}.{index}.{analyse_list("", item)}": item)
#         combined = solution.update(temp)
#
# def get_key(item, word, index):
#     if isinstance(item, list):
#         return word + f".{index}" + get_key(item[0],"", item)

def analyse_list(word, items):
    solution = {}
    for index, item in enumerate(items):
        if isinstance(item, list):
            solution.update(analyse_list(f"{word}.{index}", item))
        else:
            solution[f"{word}.{index}"] = item
    return solution
