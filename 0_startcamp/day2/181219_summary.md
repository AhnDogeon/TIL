# 1. git 사용법

* git add . 현재 상황 정지라고 생각

* git commit -m '~181218' 버젼만들기 VCS 버젼 컨트롤 시스템

* git push  깃스타그램 업로드

* git status (현재 상태)


# 2. 모닝퀴즈

```python
# # 1. 평균구하기
 my_score = [79, 84, 66, 93]
 my_average = sum(my_score, 0.0) / len(my_score) #float 타입
 print(my_average)

# #선생님 답
 my_score = [79, 84, 66, 93]
 my_total = sum(my_score)
 my_average = my_total / len(my_score)


 your_score = {
     '수학' : 87,
     '국어' : 83,
     '영어' : 76,
     '도덕' : 100
 }
 your_score.values()

 print(your_score.values())
 your_average = sum(your_score.values(), 0.0) / len(your_score.values())
 print(your_average)

#선생님 답
 your_score = {
      '수학' : 87,
      '국어' : 83,
      '영어' : 76,
      '도덕' : 100
 }

 your_total = sum(your_score.values())
 your_average = your_total / len(your_score)
 print('당신의 평균은 :', your_average)
```

* ### 최고온도 최저온도 구하는 법

  ```python
  ########## 도시 온도 평균 구하기
  cities_temp = {
      '서울' : [-6, -10, 5],
      '대전' : [-3, -5, 2],
      '광주' : [0, -5, 10],
      '구미' : [2. -2, 9]
  }
  # 3. 도시별 온도 평균
  # 서울 : ?
  # 대전 : ?
  # 광주 : ?
  # 구미 : ?
  
  ### 선생님 답
  
  for city in cities_temp: # 왼손으로 키만 꺼냅니다
      temperatures = cities_temp[city]
      avg_temperature = round(sum(temperatures) / len(temperatures),2)
      print(city, avg_temperature) # or print(city + " : " + str(avg_temperature))
      print('{0}: {1}'.format(city, avg_temperature)) #  print 문안에 바로 넣고 싶을 
  
  for key, value in cities_temp.items(): # 양손으로 둘 다 꺼냅니다
      avg_temperature = round(sum(value) / len(value), 2)
      print(key, avg_temperature)
      
      
  ### 4. 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳
  # Hottest : ??, Coldest : ??
  
  ### 내 답
  min_temp = []
  min_city = []
  for k in cities_temp:
      if k =='서울':
          low_s_temp = min(cities_temp[k])
          min_temp.append(low_s_temp)
          min_city.append(k)
      elif k =='대전':
          low_d_temp = min(cities_temp[k])
          min_temp.append(low_d_temp)
          min_city.append(k)
      elif k =='광주':
          low_k_temp = min(cities_temp[k])
          min_temp.append(low_k_temp)
          min_city.append(k)
      elif k =='구미':
          low_g_temp = min(cities_temp[k])
          min_temp.append(low_g_temp)
          min_city.append(k)
  
  
  max_temp = []
  max_city = []
  for g in cities_temp:
      if g =='서울':
          high_s_temp = max(cities_temp[g])
          max_temp.append(high_s_temp)
          max_city.append(g)
      elif g =='대전':
          high_s_temp = max(cities_temp[g])
          max_temp.append(high_s_temp)
          max_city.append(g)
      elif g =='광주':
          high_s_temp = max(cities_temp[g])
          max_temp.append(high_s_temp)
          max_city.append(g)
      elif g =='구미':
          high_s_temp = max(cities_temp[g])
          max_temp.append(high_s_temp)
          max_city.append(g)
  
  for z, vr in enumerate(max_temp):
      if (max(max_temp) == vr):
          a = z
  print('가장 온도가 높은 곳은: ', max_city[a], '의 ', max(max_temp))
  
  for x, va in enumerate(min_temp):
      if(min(min_temp) == va):
          b = x
  print('가장 온도가 낮은 곳은: ', min_city[b], '의 ', min(min_temp))
  
  
  
  ```
