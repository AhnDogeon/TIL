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

