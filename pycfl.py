import re


def pycfl(s):
    # !+[]  1
    # !![]  1
    # ![]   0
    # []    0
    result = ''
    # print(s)  # DEBUG
    ss = re.split('\(|\)', s)
    for s in ss:
        if s in ('+', ''):
            continue
        elif s[0] == '+':
            s = s[1:]
        s = s.replace('!+[]', '1')
        s = s.replace('!![]', '1')
        s = s.replace('![]', '0')
        s = s.replace('[]', '0')
        s = s.replace('+!![]', '10')
        # print(s)  # DEBUG
        result += str(sum([int(i) for i in s.split('+')]))
    return result
