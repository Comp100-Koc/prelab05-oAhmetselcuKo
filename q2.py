def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    result = ""
    for ch in s:
        if result != "" and result[-1] == ch:
            result = result[:-1]
        else:
            result += ch
    return result