# 190102 수업내용 정리

## 1. 스크래치

* 

## 2. jupyter 노트북

* cd TIL(git bash 실행)

* cd 01_python

* git clone https://github.com/eduyu/jupyter_notebooks.git

  esc누르면 파란색으로 바뀌는데 이건 커맨드모드

  초록색은 edit모드

  셀단위로 코드가 실행된다(ctrl + enter)

  커맨드모드에서 h누르면 단축키

```python
#내 코드 최대공약수 최소공배수

def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

def lcm(a, b):
    return a*b//gcd(a,b)

num1 = 4
num2 = 3


print(gcd(num1,num2))
print(lcm(num1,num2))
```



git bash에서

cd TIL

pwd

git remote -v

git add .







