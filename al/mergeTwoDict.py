'''合并两个字典'''


def merge(dict1, dict2):
    return {**dict1, **dict2}


if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3}
    print(merge(dict1, dict2))
