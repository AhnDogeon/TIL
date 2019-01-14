# html

## 월드 와이드 웹

web :  인터넷에 연결되어 있는 컴퓨터들이 정보를 주고받는 공간

get(주세요) <->ok

post(처리해주세요)<->ok



user >>>>>> program

​	request

​	<<<<<<<

​	response



우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.





서버컴퓨터 : 서버 역할을 위해 필요한 프로그램만 깔려 있다.

클라이언트 사용량에 맞는 성능을 가진다.

보안에 있어 공격대상이 되기 쉽다.

절대 꺼지지도, 인터넷 연결이 끊겨서도 안된다.



## html : 

하이퍼 링크를 통해서 텍스트 간 이동이 가능함

htper text 전송 프로토콜 : http

웹페이지를 작성하기 위한 역할 표시 언어 : html

html파일 : html로 작성된 문서파일



### static web 정적인 웹

아무것도 없는 컴퓨터에 하나만 설치해야 한다면? : 브라우저(크롬)

직접 주소창에 지정하여서 가져오는 도서관같은 웹

단, https://ahndogeon.github.io/ 뒤에 아무것도 안붙이면 정확히 'index.html' 이라고 디폴트값 주어져서 그 파일에 접근하게 한다. ---- 인덱스 페이지



### Dynamic web : web application program(web app)









모든 컴퓨터에서 서버에 달라고 하는 법 : URI(i)

URL(Uniform Resource Locator)은 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 고유 규약이다.

흔히 웹사이트 주소로 알고 있지만 url은 웹사이트 주소뿐만 아니라 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다.





## html

https://validator.w3.org/ 여기서 다이렉트 인풋에서 복붙 -> 파이썬 튜터같이 html 파일 검사해주는 곳



```html
<!DOCTYPE html> # 선언해주는 것, 지금부터 시작한다!
<html lang="en"> # html은 트리구조 en 대신 ko넣으면 시각장애인분들을 위한 읽어주는 트리거
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>AhnDogeon's github page</title>
</head>
<body> # 이 안의 내용들이 사람들한테 보여지는 내용
    <h1>Comming Soon..</h1>
</body>
</html>
```

`<h1>내용</h1> 여는 태그 닫는 태그 -----> 태그 + 내용 : 요소 (element)`

혼자 열리고 혼자 닫히는게 있음

`<img src="./animals/animal.jpg" alt="daram"/>`

속성(attribute) :  ~~ = ~~ : attribute 는 이것 속성명은 따옴표 없고 속성값은 따옴표 있다!

`<li>HTML</li>` 엘러먼트의 태그는 li이고 컨텐트는 html이고 attribute는 없습니다

h1, img, ul은 형제 자매관계이고 body와 부모자식 관계

div 들 : 요즘은 이름에 명시해줌

header : 헤더

nav : 네비게이션 바

aside : 좌측우측 사이드

footer: 하단에 있는 것

등등 div가 아니라 태그 이름만 봐도 이 문서에서 무슨 역할하는지 알 수 있게 됨 html5에서



크롬에서 web developer 

informatino에서 view document outline



html 글자 두껍게 하기

`<b></b>` 그냥 두껍게만 하는 것

`<strong></strong>` 이게 요즘 강조하는 것

`<i></i>` :

`<em></em>` 기울이기

`<blockquote></blockquote>`: 인용구 블럭

<ol> 순서가 있는 리스트





