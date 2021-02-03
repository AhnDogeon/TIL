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
    # 이건 function, class 안에 있으면 method
    def start(self):
        print(self.color)
        print("I started")

    def __init__(self, *args, **kwargs):
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "0")


# kia와 hyundai instance 생성
# intro of OOP
kia = Car()
kia.color = 'white'

hyundai = Car()
hyundai.color = 'black'

porche = Car("GREEN", "$40")
# 이대로 실행한다면 argument error가 나게 된다. 
# 파이썬에서 method의 첫번째 인자로 self를 주는데 method에는 인자가 0개라서!
# 따라서 위  method에서 self인자를 넣어줄 것
# -> 여기서 self는 instance 자신이 된다! (self.color에서 Super Red가 출력되는 것)
porche.color = "Super Red"
porche.start()