"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=840
"""

import requests #  파있너에서 url요청할 때 엔터를 담당(요청)
URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=840'

got = requests.get(URL) # get 요청보낸단 말, 엔터를 치는 행동
print(got)