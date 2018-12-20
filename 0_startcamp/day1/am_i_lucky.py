import requests # 이건 그냥 되는게 아니라 pip -v 로 받아와야한다.
import random

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



################

numbers = list(range(1,46))

my_numbers = random.sample(numbers, 6)
my_numbers.sort()

print(my_numbers)

#####################

# my_numbers, real_numbers, bonus_number
### 내 답
same_numbers = list(set(my_numbers).intersection(real_numbers))
if len(same_numbers) == 6:
        print("1등")
elif len(same_numbers) == 5:
        if bonus_number in my_numbers and len(same_numbers) == 5:
                print("2등")
        elif len(same_numbers) == 5:
                print("3등")
elif len(same_numbers) == 4:
        print("4등")
elif len(same_numbers) == 3:
        print("5등")
else:
        print("꽝")


### 선생님 답

## 방법 1. for문을 이용
count = 0
for my_numbers in my_numbers:
        for real_number in real_numbers:
                if my_number == real_number:
                        count += 1
if count == 6:
        print(1)
elif count == 5 and bonus in my_numbers:
        print(2)
elif count == 5:
        print(3)
 
## 방법 2. 집합을 이용! 집합은 set 자료구조 set은 리스트처럼 인덱스로 순서가 있는게 아님
## list = [1,2,3] 이렇게 순서로 구분
## tuple = (1,2,3)

## set = {1,2,3} 딕셔너리랑 구분해야한다, 인덱스로 접근 불가

my_numbers = set([1,2,3,4,5,6])
real_numbers = set([1,2,3,4,5,6])
bonus = 7

match_count = len(my_numbers & real_numbrs)

if match_count == 6:
        print('1등')
elif match_count == 5 and bonus in my_numbers:
        print('2등')
