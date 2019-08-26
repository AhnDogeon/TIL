# 알고리즘 day1

### APS기본 - 자료구조

### APS응용 - 알고리즘 설계

* 최적화 문제(optimization problem) : 시간 중요!
  * 최대 혹은 최소가 되는 경우를 찾는다.
  * 최적해를 찾는 문제

### 알고리즘 테스트 

* intermediate --> 정확성
* advanced --> 완전탐색

```
알고리즘 문제를 풀 때 내장함수, 라이브러리 사용하지 않는다!
ex : min, max ...
```

### swexpertacademy.com

완전검색하면 문제푸는데 너무 오래걸린다 따라서, 완전검색을 효율적으로!

* DP(dynamic programming)

* 백트래킹

* 분할정보

##### 그리고 그리디!

### 시간복잡도 ( 실행시간이 어느정도 걸리는지 표현하는 방법)

- 실행되는 명령문의 개수를 계산

  ```python
  def CalcSum(n):
      sum = 0 # 1번
      for i in range(1, n+1): # 1번
          sum = sum+i // 1번 --> 총 두 번이 n번 반복되므로 2n 
      return sum;
  ```

  ```md
  1 + n * 2 = 2n + 1
  ```

  ```python
  def CalcSum(n):
      return n * (n+1)//2 # 3번
  ```

### 빅 오(O) 표기법

시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시

​	Big-O :  최악의 경우

​	옴 : 최선의 경우

​	세타 : 최악=최선

필기 1-1 참조

* 순차검색
* 이진탐색

### 배열의 필요성



### 연습문제 1

상자 길이 N

(N-1) - i -1(같거나 더 큰 블록높이 갯수)

```python
arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
maxH = 0
for i in range(len(arr)):
    height = len(arr) -1 -i # 상자가 없을 때 낙하값
    count = 0
    for j in range(i + 1, len(arr)):
        if arr[i] <= arr[j]:
            count += 1
    height -= count
    maxH = max(height, maxH)
print(maxH)
```



ABCD  중 4개 중에 2개를 뽑아 순서없이(중복허용)해서 나열

```python
arr = "ABCD"

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i], arr[j])
```

위 코드에서는 j가 i와 중복이 안된다는 것을 계산안함

```python
arr = "ABCD"

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        print(arr[i], arr[j])
```

세 개를 뽑고 싶다!

```python
arr = "ABCD"

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        for k in range(len(arr)):
            if k == i or k == j:
                continue
            print(arr[i], arr[j])
```



## 탐욕 알고리즘









### 버블정렬

오름차순 정렬

앞의 두 수 비교하여 큰 수를 뒤로 이동. 

```python
#      0   1  2   3   4    N = 5
arr = [55, 7, 78, 12, 42]
N = len(arr)
for i in range(N - 1):
    if arr[i] > arr[i+1]:
        arr[i], arr[i + 1] = arr[i_+ 1], arr[i]

print(arr)
```

```python
for i in range(N - 2): # 최종 인덱스는 이미 최댓값이 확정이므로 N-2까지
    if arr[i] > arr[i+1]:
        arr[i], arr[i + 1] = arr[i_+ 1], arr[i]
print(arr)
```

```python
for i in range(N - 3):
    if arr[i] > arr[i+1]:
        arr[i], arr[i + 1] = arr[i_+ 1], arr[i]
print(arr)
```



* 따라서 바깥의 for문으로 위 반복과정을 해결가능

```python
arr = [55, 7, 78, 12, 42]
N = len(arr)
for j in range(N-1, 0, -1): # 위 코드에서 계속 변화하는 N - 숫자 의 값을 겉의 for문으로 구현
	for i in range(j):
    	if arr[i] > arr[i+1]:
        	arr[i], arr[i + 1] = arr[i_+ 1], arr[i]

print(arr)
```



### 카운팅 정렬

#### 순서 결정 위해 각 항목이 몇 개씩 있는지 세는 작업을 거침

제한사항 : 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능

```python
K = 4

arr = [0, 4, 1, 3, 1, 2, 4, 1]  # 원본 자료
cnt = [0] * (K + 1)

# 빈도수 계산
for val in arr:
    cnt[val] += 1
idx = 0

print(cnt)
# 위 코드의 결과값이 [1, 3, 1, 1, 2]
# 이것을 다시 0이 한 번 1이 세 번 이렇게 나누어 정렬해줌
for i in range(K + 1):
    for j in range(cnt[i]):
        arr[idx] = i
        idx += 1
        
print(arr)
# [0, 1, 1, 1, 2, 3, 4, 4]
```



### 누적빈도수

??? 교재 방식

```python
K = 4

arr = [0, 4, 1, 3, 1, 2, 4, 1]  # 원본 자료
cnt = [0] * (K + 1)
sorted = [0] * len(arr)
# 빈도수 계산
for val in arr:
    cnt[val] += 1
    
for i in range(1, K+1):
    cnt[i] = cnt[i-1] + cnt[i]

for val in range(len(arr)-1, -1, -1): # 뒤에서부터 읽는다.
    cnt[arr[val]] -= 1
    sorted[cnt[arr[val]]] = arr[val]
print(arr)
print(sorted)
```



### 배열 1 종료 후 인풋값에 따른 결과값 출력

```python
# 1번
import sys
sys.stdin = open("input1.txt", "r") # 이 두 줄로 인풋값이 저장되어 있는 텍스트파일 가져와서 인풋 입력 . 단 같은 경로에 있어야 함or 경로지정
sys.stdout = open("output.txt", "w") # 화면에 출력안되고 이 파일이 생성이 된다.

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N)
    print(arr)
```

```python
# 2번
import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr=[]
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print(N)
    print(arr)
```

```python
# 3번 다른 라인에 있을 때
import sys
sys.stdin = open("input3.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = input()
    print(N, arr)
```

```python
# 4번 같은 라인에 있어야 문자열과 정수 구별해야 할 때
import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for test_case in range(T):
    N, arr = intput().split()
    N = int(N)
    print(N, arr)
```

```python
# 정수로 저장하고 싶을 때, 문자열을 받아서 2차배열의 정수형태로 저장
import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(intput())
    arr = [[ 0 for _ in range(N) ] for _ in range(N)] # 0으로 변환?
    for i in range(N):
        tmp = input()
        for j in range(N):
            arr[i][j] = int(tmp[j])
        print(arr)


```

























​	























































































































