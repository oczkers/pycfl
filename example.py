import re
import requests
import time
from pycfl import pycfl

r = requests.Session()

rc = r.get("https://nordvpn.com/login").text
open('gdown.log', 'w').write(rc)
if 'Checking your browser before accessing' in rc:
    ans = pycfl(rc)
    jschl_vc = re.search('name="jschl_vc" value="(.+?)"', rc).group(1)
    jschl_pass = re.search('name="pass" value="(.+?)"', rc).group(1)
    params = {'jschl_vc': jschl_vc,
              'pass': jschl_pass,
              'jschl_answer': ans}
    rc = r.get('https://nordvpn.com/cdn-cgi/l/chk_jschl', params=params).text
    open('gdown.log', 'w').write(rc)
