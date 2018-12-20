import requests 
import random

#인자가 있고 리턴이 있다. / yes in yes out
#인자가 있고 리턴이 없다. / yes in no out
#인자가 업고 리턴이 있다. / no in yes out
#인자가 없고 리턴이 없다. / no in no out


## def 정의는 밑에 사용전에 위로 올려줘야 한다.
def pick_lotto():
    numbers = random.sample(range(1,46), 6) 
    return numbers

def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
    url = url + str(draw_no)
    
    response = requests.get(url) 
    lotto_data = response.json()
    numbers = []

    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    final_dict = {
        'numbers' : numbers,
        'bonus' : bonus_number
    }
    # {numbers : [1,2,3,4,5,6], bonus : 7} 이렇게 리턴해주려고 final_dict 사용
    return final_dict


#### 1단계
# def am_i_lucky(pick, draw):
#     match_count = set(pick) & set(draw)
#     if len(match_count) == 6:
#         return('1등')
#     elif len(match_count) == 5 and bonus in my_numbers:
#         return('2등')
#     elif len(match_count) == 5:
#         return('3등')
#     elif len(match_count) == 4:
#         return('4등')
#     elif len(match_count) == 3:
#         return('5등')
#     else:
#         return('꽝')

# print(am_i_lucky([1,2,3],[1,2,4]))

### 2단계
def am_i_lucky(pick, draw):
    match_count = set(pick) & set(draw['numbers']) ## 위 1차랑 다른 점 draw 자리가 딕셔너리이므로
    if len(match_count) == 6:
        return('1등')
    elif len(match_count) == 5 and draw['bonus'] in pick: ## 위랑 같은 이치로
        return('2등')
    elif len(match_count) == 5:
        return('3등')
    elif len(match_count) == 4:
        return('4등')
    elif len(match_count) == 3:
        return('5등')
    else:
        return('꽝')


result = am_i_lucky(pick_lotto(), get_lotto(837))
print(pick_lotto())
print(get_lotto(837))
print(result)