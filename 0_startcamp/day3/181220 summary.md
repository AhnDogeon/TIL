# 181220 수업정리

## 1. html

* h1은 가장 큰 제목으로 사용. 가장 중요하다고 생각하는 제목에 써주는 것. 단순히 글자크기가 아니다
* 모든 태그는 의미가 있다.
* 마크업에서 태그들이 가지는 의미는 ``역할을 지정`` 
* h1은 무 조 건 써야한다.

## 2. 로또 마무리

* ```python
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
  
          
  ```

* ## 위 로또 코드를 기능 영역별로 깔끔하게 정리하고 싶다!   def이용! : 리팩토링

     ```python

     ```

* ```python
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
  ```

* 함수는 return 하는게 있고 없는게 있다. 위 소스 pick_lotto의 return 값 참조. 

  * return 해줘야 값을 주고 받을 수 있다

  * 단, a = sorted([3,2,1]) , b = [3,2,1].sort() 와 같이 a는 return 값 존재, b는 none 출력

    ```python
    a = sorted([3,2,1])
    b = [3,2,1].sort()
    print(a,b)
    
    ## 결과는 [1,2,3] None
    ```

* 다른 파일에 만들어둔 def 함수 쓰기 : import (def가 저장되어있는) 파일이름

```python
### math_functions.py 안에 있는 cube와 average 쓰기

import math_functions

print(math_functions.cube(5))
print(math_functions.average([10,20,30,]))

### 이렇게 하면 math_functions 안에 def 로 정의되어 있는 것이 다 딸려오고 실행된다 따라서 우리는
from math_functions import cube, average

print(cube(5))
print(average([10,20,30,]))

### 그렇게 해도 math_functions 의 메인문들이 실행이 된다
def main():
    my_score = [79, 84, 66, 93]
    print(average(my_score))
    print(cube(3))

if __name__ == '__main__':
    main()
## 그럴 때 math_functions 에 위 구문을 넣어주면 해결





```



* ## 마지막 check_lotto 최종파일

  * ```python
    from lotto_functions import am_i_lucky, pick_lotto, get_lotto
    
    result = am_i_lucky(pick_lotto(), get_lotto(837))
    print(result)
    ```
