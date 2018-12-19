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

del(team[2]) # 인덱스 2위치의 'neo'가 날아감 삭제!
del(team[2:4])#인덱스 2부터 3까지 날아감