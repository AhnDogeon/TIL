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


