def remove_duplicates(lst):
    result = []
    for n in lst:
        if n not in result:
            result.append(n)
    return result
