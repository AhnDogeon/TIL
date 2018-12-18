import requests # 이건 그냥 되는게 아니라 pip -v 로 받아와야한다.

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) #요청에 대해서 튀어나온 것
#print(response.text)

# 하지만 response.text는 string 문자열이므로 딕셔널화 해야한다. aka 파씽

lotto_data = response.json()

# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6']
# ] 현명하지 못한 코딩
real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])#lotto_data[key] 가 value이므로

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value) # key 와 value 를 동시에 입력하려고 할 때 items()를 사용한다.

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)