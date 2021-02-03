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
    
    def __str__(self):
        return f'Car With {self.wheels} wheels'


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

# 상속! 클래스를 인자로 넣어 상속받으면 Car Class의 Property 사용 가능
# Django를 이용하여 다시 프로젝트를 진행할건데 Class의 이러한 상속 개념을 알아두면 좋을듯
class Convertible(Car):
    def __init__(self, *args, **kwargs):
        # 이렇게 사용하면 __init__가 재정의가 되어 Car에서 Init한 color는 사용하지 못하게 된다.
        # 이를 방지하기 위해 super 함수 사용(부모 함수를 호출)
        super().__init__(**kwargs)
        self.time = kwargs.get("time",10)

    def take_off(self):
        return "taking off"

    # Car의 __str__을 Override
    def __str__(self):
        return f'Car With no roof'

ferrari = Convertible("GREEN", "$40")

ferrari.take_off()
ferrari.wheels = 5
# super 함수로 부모 클래스의 init 메소드를 가져와서 사용가능
print(ferrari.color)