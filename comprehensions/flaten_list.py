def filter_elements(lst):
    return [e for e in lst.split() if e != " "]


def flatten_list() -> str:
    result = [filter_elements(item) for item in input().split("|")[::-1]]
    return " ".join(e for row in result for e in row)


print(flatten_list())
