import re
import time


def _cf(s):
    # !+[]  1
    # !![]  1
    # ![]   0
    # []    0
    # +!![] 10
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
        # print(result)
    return int(result)


def cf(s):
    ss = re.split('/', s)
    result = _cf(ss[0])
    for i in ss[1:]:
        # print(i)
        result /= _cf(i)
    # print('result: %s ' % result)
    return result


def pycfl(html):
    host = re.search('Checking your browser before accessing</span> (.+?)\.</h1>', html).group(1)
    ans = re.search('.+?={".+?":([+/\(\)!\[\]]+)};', html).group(1)
    ans = cf(ans)
    # print('ans: %s' % ans)
    for i in re.findall('.+?\..+?([*+-]{1})=([+/\(\)!\[\]]+);', html):
        if i[0] == '*':
            ans *= cf(i[1])
        elif i[0] == '+':
            ans += cf(i[1])
        elif i[0] == '-':
            ans -= cf(i[1])
        # elif i[0] == '/':
        #     ans /= _cf(i[1])
    ans = round(ans + len(host), 10)
    time.sleep(4.5)  # 4 is enough?
    return ans
