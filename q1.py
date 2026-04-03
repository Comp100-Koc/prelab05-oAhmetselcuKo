def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    lsubs = ""
    n = len(s)
    for i in range(n):
        for k in range(i + 1, n):
            sub = s[i:k+1]
            if sub == sub[::-1]:
                if len(sub) >= 2 and len(sub) > len(lsubs):
                    lsubs = sub
    return lsubs