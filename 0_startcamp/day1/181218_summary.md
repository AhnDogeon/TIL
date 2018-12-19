# 181218 안도건 수업정리**

## 1. 개발환경설정

* chocolatey 설치
  * 윈도우 패키지 매니저
* python -v 3.6.7
* git
  * version control system
* vscode
  * code - editor
* chrome

## 2. cd : change directory

* ~ : home 을 의미 --- cd ~ 엔터
* ls : list 그 경로 밑의 폴더 보여줌
* cd / : 내 pc 최상단
* mkdir : 그 경로의 새폴더만들기
* rmdir : 그 경로의 폴더지우기
* touch first _python.py : first_python.py라는 파일 만들기



## 3.python first_python.py 엔터 : first_python.py 실행

## 4. ctrl + L or clear :  깔끔하게 정리

## 5. 리스트 

* 리스트 안에는 family =['mom', 1.64, 'dad', 1.75, 'sister', 1.78, True] 식으로 안에 어떤 타입이 와도 상관은 없다

* 리스트에서 제일 마지막에 접근하려면 -1

* ```python
  mcu = [
  
      ['ironman', 'captain'],
  
      ['xmen','deadpool'],
  
      ['spiderman']
  
  ] 
  ```

  에서 하나의 요소에 접근하려면

  ```python
  mcu[0][1]
  ```

   이렇게 접근해야함

* 리스트 안은 쉼표로 무조건 구분해야한다.

* list 추출하기

  * 

* list 연산

  * ```python
    team = [
        'john', 10000,
        'neo', 100,
        'tak', 40500
    ]
    
    team[2:4] #neo와 100이 튀어나온다
    
    type(team[2:4]) #타입이 list가 튀어나온다
    team[2:3] # ['neo'] 가 나옴
    team[2] # 'neo' 만 나옴
    
    new_member = ['js', 10]
    
    team = team + new_member #list끼리 덧셈연산 가능하다, 우측 결과값을 왼쪽에 넣는다
    #team 은 이렇게 나옴 : ['john', 10000, 'neo', 100, 'tak', 40500, 'js', 10]
    
    #list끼리 덧셈연산하면 list가 그 안으로 뒤에서 합쳐짐
    team += new_member #위 team = team + new_member와 같은 코드다
    ```

  * list에서 삭제

    * ```
      del(team[2]) # 인덱스 2위치의 'neo'가 날아감 삭제!
      
      del(team[2:4])#인덱스 2부터 3까지 날아감, 통째로 여러개 지울 때
      ```



## 6. '123' 은 문자

* 단, int('123') 은 숫자 123으로 변환시켜줌
* 같은 의미로 range(1,46)을 list(range(1,46)) 으로 넣어주면 list 형식으로 바뀜
* 모든 타입변환이 가능한 것은 아니다. 타입캐스팅

## 7. numbers [5:10]

* list에서 인덱스 5에서 인덱스 10전까지 0 1 2 3 4 5 6 7 8 9 10 11 12 이면 5부터 9까지
* [start:end] start 는 포함하며 end는 안포함
* number[1:10] : 1부터 9까지라는말

## 8. dictionary

* {}로 이루어져 있다.

* 딕셔너리 안의 자료 접근하기 

  ```python
  my_info = {
                  'name':'neo',
                  'job' : 'hacker',
                  'mobile' : '01012345678',
                  'email' : 'neo@hphk.kr'
  }
  hphk = [
      {
          'name' : 'john',
          'email' : 'john@hphk.io'
      },
      {
          'name' : 'neo',
          'email' : 'neo@hphk.io'
      }
      {
          'name' : 'tak', #딕셔너리는 키와 : 딕셔너리로 이루어짐
          'email' : 'tak@hphk.io'
      }
  ]
  p = hphk[2]
  print(type(p))
  print(p['name'])
  hphk[2]['name']
  
  ```

## 9. Function

```python
print('hi')
len('hi')
len([1,2,3,4,5]) # 5
scores = [45, 60, 78, 88] 
high_score = max(scores) # scores 리스트의 가장 큰 값을 뽑아내는 함수
lowest_score = min(scores)

round(1.8) # 답은 2 : 반올림
round(1.4) # 1

round(1.876, 2) # 소수점 둘째자리까지 반올림

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full에 first 와 second 을 합쳐서 저장
full = first + second
# full_sorted 에 full을 정렬해서 저장
full_sorted = sorted(full)
# *reverse_sorted  에 full을 내림차순으로 정렬해서 저장
reverse_sorted = sorted(full,reverse = True)



```

# 10. Method

* 메서드는 함수다! 다만 **[주어].동사()**의 형식으로 이루어지며, [주어] 자리에 오는 object들이 할 수 있는 행동(함수)들이다.

* .으로 이어져 있으면 앞의 클래스나 리스트 등등에 종속되어있는 것, 얘도 함수임

* ```python
  my_list = [4,7,9,1,3,7,6]
  # 최댓값
  max(my_list)
  min(my_list)
  # 특정 요소의 인덱스. my_list 에서 3이 몇 번째인지
  my_list.index(3)
  # 특정 요소가 몇 개 있는지
  my_list.count(3)
  
  # 리스트를 통째로 뒤집으려면?
  my_list.reverse()
  
  dust = 100
  language = 'python'
  samsung = ['elec', 'sds', 's1']
  
  lang = 'python'
  lang.capitalize() # lang의 문자열 첫번째를 대문자로 바꿔준다, 단, 기존의 lang이 아예 Python으로 바뀌는건 아님
  lang.replace('on', 'off') # python의 on을 off로 바꿔줌, 이것 또한 기존의 lang은 바뀌지 않는다
  
  #단, 원본이 바뀌는 경우도 있다.
  l = [3, 2, 1]
  l.sort() # 이 경우 주어를 냅두고 이 문장을 쳐서 추출하는 것이 아니라, 원래 주어가 바뀌어버림. l = [1,2,3]
  
  
  samsung.append('bio') # 얘도 원본이 바뀜, 평소의 samsung + 'bio'안해도 된다
  # 얘는 기억하자! 자주 쓴다 append
  
  
  ```

* | str      | int  | list           | bool  | <=Class   |
  | :------- | ---- | -------------- | ----- | --------- |
  | 'python' | 100  | ['a', 3, True] | False | <= Object |

  # 11. webbrowser

  * ```python
    import webbrowser # 사용하는 구문보다 무조건 앞에 있어야 함
    
    keywords = [
        '사당 맛집',
        '영화 순위',
        '옷'
    ]#검색하고 싶은 것을 넣는다
    
    for keyword in keywords: #콜론이 있으면 들여쓰기
        url = 'https://www.google.com/search?q=' + keyword
        webbrowser.open_new(url)
    
    
    ```

  * 

# 12. lotto

* pick_lotto.py : 기존 로또 번호 6개 랜덤 뽑기

  ```python
  import random
  
  numbers = list(range(1,46))
  
  my_numbers = random.sample(numbers, 6)
  my_numbers.sort()
  
  print(my_numbers)
  
  
  ```


* get_lotto.py : 로또 홈페이지 api로 정보 요청하여 가져오기

  ```python
  import requests # 이건 그냥 되는게 아니라 pip -v 로 받아와야한다.
  
  url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
  
  response = requests.get(url, verify = False) #요청에 대해서 튀어나온 것, verify = false는 사이트마다 보안인증서의 차이가 있으므로 그게 필요없을 때
  print(response.text)
  
  
  ```

  단, requests 요청하려면 pip -v 이후에 pip install requests 를 실행시켜주어야 한다.

* ```python
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
  print(real_numbers)
  ```

  * ```python
    ###과제입니다
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
    
    for number in my_numbers:
        cor_number = len(set(number)&set(self.real_numbers[:6]))
    # 1 등 : 
    if cor_number == 6:
                    print('\t{:2} {:2} {:2} {:2} {:2} {:2}'.format(*i[:6]),end=' >>> ')
                    print('1등 당첨')
                    self.rank[0] += 1
    # 2 등 : real & my 가 5개가 같고, my의 나머지 하나가 bonus_number
    
    # 3 등 : real & my 가 5개가 같다.
    
    # 4 등 : real & my 가 4개가 같다.
    
    # 5 등 : real & my 가 3개가 같다.
    
    # 꽝
    ```

  * 



  # 13. weather

  * json viewer 크롬 다운받기

  * pip install darkskylib 처럼 쉽게 받을수도 있음(pypi라는 사이트에서)

  * ```python
    # import requests
    # # url = 'https://api.darksky.net/forecast/7214b67b19c9d40bfa0d8d64ec638240/37.501826,%20127.039649'
    
    # # res = requests.get(url)
    # # data=res.json()
    
    # # print(data)
    # # print(data['currently']['summary'])
    
    
    ## pypi를 통한 조금 더 쉬운 api 따오기
    from darksky import forecast
    multicampus = forecast('7214b67b19c9d40bfa0d8d64ec638240', 37.501311, 127.037471)
    print(multicampus['currently']['summary'])
    print(multicampus['currently']['temperature'])
    
    ```

  # 14. git

  * git init으로 마스터 지정.

  * rm -rf .git/ 으로 git  지정 탈퇴
  * git commit -m ''~181218' 버젼만들기 VCS 버젼 컨트롤 시스템
  * 