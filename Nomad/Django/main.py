# positional arguments, keyword arguments 차이
# Django를 사용할 때, 이와 같이 여러 인자를 받아야 하는 경우(무한대) 사용
# *args **kwargs
def plus(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b 

print(plus(3, 4, 1,1,1,1,1,1,1,1,hello=True, dasf='sda', vvv=False))

# Object Oriented Programming 객체지향 프로그래밍
class Car():
    wheels = 4
    door = 4
    windows = 4
    seats = 4

# kia와 hyundai instance 생성
# intro of OOP
kia = Car()
kia.color = 'white'

hyundai = Car()
hyundai.color = 'black'
