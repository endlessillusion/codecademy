def purify(lst):
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return result
