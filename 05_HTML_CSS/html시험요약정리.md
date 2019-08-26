# 28일 시험 요약

## HTML & CSS

- HTML 파일 제공.
- 예시 결과를 보고 CSS를 직접 작성해서 HTML Tag에 적용하는 형식. (주로 텍스트를 꾸미는 형식, 수업시간 및 프로젝트에서 자주 사용했던 속성들 위주로 출제)
- tag 선택자, class 선택자, id 선택자만 사용해도 되도록 출제.
- position, display, background-image 같은 속성들은 출제 안됨.
- class 선택자, id 선택자를 이용하여 작성한 CSS를 HTML Tag에 적용하는 방법 숙지 필요.



css 적용법 세 가지(시험에 아마 외부참조 형식으로 나올 듯)

* inline(비추천)

  ```html
  <h1 style="color: blue; font-size:100px">
      Hi
  </h1>
  ```

* html 파일 head 태그 안(내부참조)

  ```html
  <style>
      h1 {
          color: blue;
          font-size: 100px
      }
  </style>
  ```

* link file(외부참조)-이걸로 나올 듯

  html 파일 head 안에

  ```html
  <head>
      <link href="style.css" type="text/css" rel="stylesheet">
  </head>
  ```

  해준 후 mystyle.css 파일 안에서 css 적용

  ```css
  h1 {
  	color: blue;
  	font-size:20px
  }
  ```

  

### 태그 선택자

```html
p { color: darkgoldenrod;}

h2, h3 { background-color: lightgray;} # 여러 개 선택 가능
```

### id/ class_selector (id, class 선택자)

- css 에서는 id는 최대한 안 불러오는게 맞다
- css 에서는 class로 불러와서 작업할 것!

| 패턴   | Description                                                  |
| ------ | ------------------------------------------------------------ |
| #id    | id 어트리뷰트 값을 지정하여 일치하는 요소를 선택<br />(id 어트리뷰트 값은 중복될 수 없다) |
| .class | class 어트리뷰트 값을 지정하여 일치하는 요소를 선택<br />(class 어트리뷰트 값은 중복될 수 있다.) |

![idclass](C:/Users/ahn_q/ryungs/TIL/05_HTML_CSS/05_HTML_CSS%EC%A0%95%EB%A6%AC/assets/idclass.PNG)



```css
.box {
    border-radius: 6px; # 모서리 둥글게
    
}
```



















## Bootstrap

- Grid System에 관한 문제를 출제.
- 미리 작성된 HTML 파일 제공. (CDN을 통하여 Bootstrap도 추가되어 있음)
- 예시 결과를 보고 알맞는 클래스를 채워 넣는 형식.
- Bootstrap 사이트 접속 불가능.
- Responsive Grid를 위한 Breakpoint 관련 내용은 문제에서 주어짐.
- 공식문서를 반드시 볼 것. (최소한 Grid의 Offsetting columns까지, 세로 정렬은 출제 안됨.)



## Django

* [R]ead(List, Detail), [D]elete(Delete) 중에 하나를 작성하는 문제 출제.

* Django 프로젝트 코드 제공. (runserver를 통한 서버 실행은 불가능)

* `views.py`에 새로운 함수 작성하여 페이지 만드는 법, template(html) 파일 만드는 법 숙지 필요.

* Django Template Language의 기본적인 사용법, '반복문', '조건문', '템플릿 상속(extends)', '페이지 출력(render)' 숙지 필요.

* 부분 점수를 위해서 최대한 많이 작성할 것.

  