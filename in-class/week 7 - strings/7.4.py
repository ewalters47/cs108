def strip_non_alpha(s):

    result = ''

    for c in s:
        if c.isalpha():
            result += c

    return result



print(strip_non_alpha('Hello!45'))