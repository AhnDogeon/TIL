#-*-coding:utf-8 -*-
import requests
import urllib.request
import csv
import json
from time import sleep

naver_URI = 'https://openapi.naver.com/v1/search/movie.json?query='
client_id = 'sc1OuIXuNEyPHrKuFavw'
client_secret = '9kBLWeULil'
headers = {'X-Naver-Client-Id' : client_id ,'X-Naver-Client-Secret': client_secret}

code = {'20184105': '말모이', '20176251': '내안의 그놈', '20189463': '주먹왕 랄프 2: 인터넷 속으로', '20180290': '아쿠아맨', '20183915': '극장판 공룡메카드: 타이니소어의 섬', '20185485': '보헤미안 랩소디', '20184574': '그린 북', '20186281': '범블비', '20170658': 'PMC: 더 벙커', '20175547': '스윙키즈', '20183785': '점박이 한반도의 공룡2 : 새로운 낙원', '20184187': '언니', '20182421': '그린치', '20168773': '마약왕', '20183479': '극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~', '20183238': '스파이더맨: 뉴 유니버스', '20177552': '국가부도의 날', '20179230': '도어락', '20183375': '극장판 포켓몬스터 모두의 이야기', '20189843': '호두까기 인형과 4개의 왕국', '20182082': '부탁 하나만 들어줘', '20178825': '모털 엔진', '20183745': '런닝맨 : 풀룰루의 역습', '20177538': '완벽한 타인', '20184481': '성난황소', '20181905': '후드', '20176814': '신비한 동물들과 그린델왈드의 범죄', '20183073': '베일리 어게인', '20181171': '바울', '20183007': '거미줄에 걸린 소녀', '20182966': '투 프렌즈', '20183050': '번 더 스테이지: 더 무비', '20182935': '출국', '20182669': '툴리', '20186822': '너의 췌장을 먹고 싶어', '20170513': '동네사람들', '20189869': '해피 투게더', '20174981': '창궐', '20010291': '해리포터와 마법사의 돌', '20179006': '여곡성', '20181404': '벽 속에 숨은 마법시계', '20180523': '스타 이즈 본', '20182693': '구스범스: 몬스터의 역습'}


for moviecode in code.keys():
    final_result = []
    imageurl = []
    res = requests.get(naver_URI + code[moviecode], headers=headers)
    naverdata= res.json()
    navermovie_url = naverdata['items'][0]['image']
    
    urllib.request.urlretrieve(navermovie_url, f'images/{moviecode}.jpg')
    sleep(0.1)


