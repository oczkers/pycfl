import re
import requests
import time
from pycfl import pycfl as _cf

r = requests.Session()

rc = r.get("https://nordvpn.com/login").text
open('gdown.log', 'w').write(rc)
if 'Checking your browser before accessing' in rc:
    host = re.search('Checking your browser before accessing</span> (.+?)\.</h1>', rc).group(1)
    ans = re.search('.+?={".+?":([+\(\)!\[\]]+)};', rc).group(1)
    ans = _cf(ans)
    for i in re.findall('.+?\..+?([*+-]{1})=([+\(\)!\[\]]+);', rc):
        if i[0] == '*':
            ans *= _cf(i[1])
        elif i[0] == '+':
            ans += _cf(i[1])
        elif i[0] == '-':
            ans -= _cf(i[1])
    ans = ans + len(host)
    # print(f'ans: {ans}')
    print('ans: %s' % ans)
    time.sleep(5)  # 4 is enough?
    jschl_vc = re.search('name="jschl_vc" value="(.+?)"', rc).group(1)
    jschl_pass = re.search('name="pass" value="(.+?)"', rc).group(1)
    params = {'jschl_vc': jschl_vc,
              'pass': jschl_pass,
              'jschl_answer': ans}
    rc = r.get('https://nordvpn.com/cdn-cgi/l/chk_jschl', params=params).text
    open('gdown.log', 'w').write(rc)
