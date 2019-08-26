[TOC]

# HTML & CSS

## 01. HTML

### 01-01 Basic Web

* Web은 기본적으로 `request` 와 `response` 로 이루어진다
* `IP` : 8비트(0-255)까지의 숫자로 구성된 숫자의 집합으로 주소를 의미
* `Domain` : 네트워크상의 컴퓨터를 식별하는 호스트명
* `URL` : 실제로 서버에 저장된 자료의 위치



### 01-02 Structure of HTML

* Basic structure

```html
<!DOCTYPE html>                  ─ DOCTTYPE 선언부
<html lang="ko">   
</html>
<head>                           ┌ head 요소
	<meta charset="UTF-8">		 | 문서 제목, 문자코드(인코딩)과 같은 문서 정보를 담고 있다
	<title>Document</title>		 | but 브라우저에 나타나지 않는 영역
</head>                          └ og와 같은 메타태그 선언이 이뤄지는 곳

<body>                           ┌ boday 요소                 
    							 │ 브라우저 화면에 나타나는 정보
</body>                          └ 실제 내용에 해당하는 곳
</html>
```



### 01-03 Semantic Tags

* 의미: '의미의, 의미론적인'이라는 뜻으로 태그만 보고도 태그 안에 들어갈 내용을 유추 가능

  * `<div>`, `<span>`... : non-semantic tag
  * `<table>`, `<article>`... : semantic tag

* HTML이 제공하는 Semantic tag

  * `<article>`, `<aside>`, `<details>`, `<header>`, `footer`, `nav`, `section`, `time` 등등..

  

### 01-04 Basic Tags

* `<a>` 

  ```html
  <a href="https://www.naver.com">go to naver.com</a>
  ```

  

* `<form>`

  ```html
  <form action="<backend-url>" method="<POST> or <GET>">
      <input type="text" name="name" value="value">
      <input type="password" name="name" value="value">
      <input type="radio" name="name" value="value">
      <input type="checkbox" name="name" value="value">
      <textarea name="name"></textarea>
      <input type="submit" value="submit">
      <select>
          <option value="1">1</option>
          <option value="2">2</option>
      </select>
  </form>
  ```



* `<img>`

  ```html
  <img src="<image_path>/<image_name>" alt="when no img">
  ```



* `<table>`

  ```html
  <table>
  	<thead>								<!-- table head -->
  		<tr>							
  			<th>학교</th>
  			<th>창립년도</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>							<!-- first table row -->
  			<td>서울대학교</td>
  			<td>1946</td>
  		</tr>
  		<tr>							<!-- second table row -->
  			<td>고려대학교</td>
  			<td>1905</td>
  		</tr>
  		<tr>							<!-- third table row -->
  			<td>연세대학교</td>
  			<td>1885</td>
  		</tr>
          <tr>
              <td colspan="2">가로로 2칸 병합</td>
          </tr>
          <tr>
              <td rowspan="2">세로로 2칸 병합</td>
          </tr>
  	</tbody>
  </table>
  ```



* `ol>li` or `ul>li`

  ```html
  <ol>						<!-- ordered list -->
  	<li>목록1</li>		  	<!-- first list -->
  	<li>목록2</li>		  	<!-- second list -->
  </ol>
  
  <ul>						<!-- unordered list -->
  	<li>목록1</li>		  	<!-- first list -->
  	<li>목록2</li>		  	<!-- second list -->
  </ul>
  ```

  



### 01-05 Box model

#### (A) Basic Concept : "All of elements in page are Box "

* Box = `margin` + `boarder` + `padding` + `box(width*height)` 

* `height` & `width` : 기본적으로 지정하지 않는다면 default 값을 가진다

  * `height`
    * default 값은 content에 의해 결정된다
    * content 크기만큼 수직으로 늘어나고 줄어든다
  * `width`
    * default of **block element** : width = 100%
    * default of **inline element** : content가 차지하는 만큼 수평으로 늘어나고 줄어든다

* `margin` & `padding` : 브라우저마다 다른 default 값을 가진다
  * `margin`
    * border 바깥에 위치
    * 페이지의 특정 위치에 element가 배치되는 것을 돕거나 다른 element와 거리를 두도록 여백 설정
  * `padding`
    * border 안에 위치
    * element의 background를 상속
    * element 안에 여백을 제공

* `border` 

  * padding 과 margin 사이에 위치

  * element 주위의 outline을 제공

  * 모든 border는 width, style, color의 세가지 값이 필요

    * `border-width` : border의 두께
    * `border-style` : 실선, 점선 등 스타일 (실선=solid)

    * `border-color` : border의 색깔



#### (B) Float : 웹페이지의 flow의 한 부분으로 남도록 설정

[About Float]: https://techbug.tistory.com/181

* float 속성 ( in CSS )

  * `float: right;` 
  * `float: left;` 
  * `float: none;` 
  * `float: inherit;` 

  

#### (C) Position : static, relative, fixed, absolute

* `static` 

  * default 값으로서 특별한 방식으로 위치가 지정된 것은 아니다

* `relative` 

  * 별도의 property(top, bottom, left, right)을 지정하지 않는다면 static과 동일

  * 원래 차지하고 있던 위치를 기준으로 property 값에 따라 위치가 이동

    * 이동하기 전에 차지하고 있던 공간은 blank가 되어도 다른 element가 차지하지 못한다

  * property 

    * `top` : top으로부터 설정한 값만큼 아래로 떨어진 위치로 element를 이동

    * `bottom` : bottom에서 설정한 값만큼 위로 떨어진 위치로 element를 이동

    * `right` : right에서 설정한 값만큼 왼쪽으로 떨어진 위치로 element를 이동

    * `left` : left에서 설정한 값만큼 오른쪽로 떨어진 위치로 element를 이동

    * example 

      ```css
      .relative {
          position: relative;
          top: -20px;		top으로부터 아래로 -20px만큼 떨어진 곳으로 이동
          left: 20px;     left로부터 오른쪽으로 20px만큼 떨어진 곳으로 이동
      }
      ```

* `fixed` 

  * viewport에 상대적으로 위치가 지정된다 ( 브라우저 기준 위치 고정 )
  * 페이지가 스크롤되더라도 늘 같은 곳에 위치
  * property로 top, bottom, left, right를 갖는다
    * `top` : top으로부터 설정한 값만큼 아래로 떨어진 위치에 element를 고정
    * `bottom` : bottom에서 설정한 값만큼 위로 떨어진 위치에 element를 고정
    * `right` : right에서 설정한 값만큼 왼쪽으로 떨어진 위치에 element를 고정
    * `left` : left에서 설정한 값만큼 오른쪽로 떨어진 위치에 element를 고정

* `absolute` 

  * viewport가 아닌 **가장 가까운** 곳에 위치한 **parent element**에 상대적으로 위치가 지정
    * 단 static인 parent element는 대상으로 고려하지 않는다
    * parent element가 없을 경우 최상위 요소인 **본문(document body)**가 기준
  * property로 fixed와 동일하게 top, bottom, left, right를 갖는다



### 01-06 Inline / Block

#### (A) Inline level element

* `span`, `a`, `strong`, `img`, `br`, `input`, `select`, `textarea`, `button`
* 새로운 라인에서 시작하지 않으며, 문장의 중간에 줄바꿈 없이 들어갈 수 있다
* content의 너비만큼 가로폭을 차지한다
  * Box가 아니기 때문에 width, height, margin, padding-top/bottom을 property로 가질 수 없다
  * 단 상/하 여백은 line height로 지정 가능 ( 한 라인의 글자간격을 설정하는 방식 )
* inline element 안에 block element를 넣을 순 없다 ( block element 안에 inline element)



#### (B) Block level element

* `div`, `h1-h6`, `p`, `ol, ul > li`, `hr`, `table`, `form`
* 항상 새로운 라인에서 시작한다
* 화면 전체 크기의 가로폭을 차지한다 (default: width 100%)
* width, height, margin, padding 등의 property 설정이 가능



#### (C) Inline-Block level element

* 사용법

```css
.inline-block {
    display: inline-block;
}
```

* Block과 Inline element의 특징을 모두 갖는다
  * Block들이 inline의 특성을 갖게 되어 한 라인에 줄바꿈 없이 들어갈 수 있다
    * Block들의 margin과 padding이 0으로 지정된다
    * margin과 padding 값을 변경하여 원하는대로 layout할 수 있다
    * 라인에 있는 block들 중 가장 큰 block의 높이를 default 높이로 갖는다
    * content의 너비만큼 가로폭을 갖는다
    * height와 width를 변경할 수 있다
  * element 뒤에 공백이 있을 경우 자동으로 space를 차지한다



## 02. CSS

### 02-01 길이단위

- Basic Units
  - `px` : 모니터의 가로/세로를 이루고 있는 격자 중 하나의 크기를 뜻한다
  - ` pt` : 1 point = 1/72 inch 로 1 pt~72 pt까지 있다 
  - `%` : 상위요소(parent element) 에 대한 상대적인 비율을 의미
  - `em` : **상위 요소 (parent element)**의 **폰트 크기**를 기준으로 한 상대적인 크기
    - ex) 상위 div의 font-size가 18px일 때 1em은 18px 값을 갖는다
  - `rem` :  **최상위 요소 (html)**의 **폰트 크기**를 기준으로 한 상대적인 크기
    - ex) html의 font-size가 16px일 때 1rem은 16px 값을 갖는다
- Browser based Units
  - `viewport` : **브라우저**의 가로 or 세로 크기에 따라 변하는 폰트 단위 
    - `vw (viewport width)` : 브라우저의 **가로폭**을 기준으로 결정되는 크기
      - ex) 브라우저의 width=1280일 때 1vw = 12.8px
    - `vh (viewport height)` : 브라우저의 **세로폭**을 기준으로 결정되는 크기 
      - ex) 브라우저의 height = 600일 대 1vh = 6px
    - `vmin (viewport minimum)` : 가로폭과 세로폭 중 더 작은 값을 기준으로 결정되는 크기
    - `vmax (viewport maximum)` : 가로폭과 세로폭 중 더 큰 값을 기준으로 결정되는 크기



### 02-02 Selector

#### (A) Universal selector

```css
* {color: red;}
```



#### (B) Tag selector

```css
p {color: red;}
div {color: red;}
```



#### (C) Id/Class selector

* id

  ```css
  #<id_name> {color: red;}
  ```

* class

  ```css
  .<class_name> {color: red;}
  ```

  

#### (D) Attribute selector

* `href`를 갖는 모든 a 태그

  ```css
  a[href] {color: red;}
  ```

  

* `target="_blank"` 를 갖는 모든 a 태그

  ```css
  a[target="_blank"] {color: red;}
  ```



*  href가 ".net"으로 끝나는 모든 a 태그

  ```css
  a[href$=".net"] {color: red;}
  ```

  

*  title에 "str" 문자열이 있는 모든 p 태그

  ```css
  p[title~="str"] {color: red;}
  
  <p title="str is"></> css 적용
  <p title="stris"></>  css 미적용
  ```



*  title에 "str"이 포함되어 있는 모든 p 태그

  ```css
  p[title*="str"] {color: red;}
  
  <p title="str is"></> css 적용
  <p title="stris"></>  css 적용
  ```

  

*  title에 "str"과 바로 이어서 -가 오는 모든 p 태그 ( "str"도 잡는다 )

  ``` css
  p[title|="str"] {color: red;}
  
  <p title="str"></> 		  css 적용
  <p title="str-first"></>  css 적용
  ```



*  title이 "str"로 시작하는 모든 p 태그

  ```css
  p[title^="str"] {color: red;}
  ```



#### (E) Combinator selector

* div element의 후손(n level) element에서 모든 p 태그

  ```css
  div p {color: red;}
  ```



* div element의 자식(1 level) element에서 모든 p 태그

  ```css
  div>p {color: red;}
  ```



* p의 sibling element 중 바로 뒤에 오는 ul 태그

  ```css
  p + ul {color: red;}
  ```



* div의 sibling element 중 뒤에 오는 p 태그

  ```css
  div ~p {color: red;}
  ```

  

#### (F) Pseudo selector : User action

* `a` tag

  * hover

    ```css
    a:hover {font-weight: bold;}
    ```

  * unvisited a tag

    ```css
    a:link {color: red;}
    ```

  * visited a tag

    ```css
    a:visited {color: red;}
    ```

  * on_clicked a tag

    ```css
    a:active {color: red;}
    ```



* `input` tag

  * focused on input tag

    ```css
    input:focus {color: red;}
    ```

  * focused on input tag whose type are text and passward

    ```css
    input[type="text"]:focus, input[type="password"]:focus {color: red;}
    ```

  * enabled input

    ```css
    input:enabled {color: red;}
    ```

  * disabled input

    ```css
    input:disabled {color: red;}
    ```

  * checked input

    ```css
    input:checked {color: red;}
    ```



#### (G) Pseudo selector : Structural

* child element

  ```css
  p:first-child {color: red;}  			/* 첫째 자식인 p tag 모두 */
  p:last-child {color: red;}	 			/* 마지막 자신인 p tag 모두 */
  ol>li:nth-child(2n) {color: red;}	    /* ol의 자식 중 짝수번째가 li라면 */
  ol>li:nth-child(2n+1) {color: red;}     /* ol의 자식 중 홀수번째가 li라면 */
  ol>li:first-child {color: red;} 	    /* ol의 자식 중 첫번째가 li라면 */
  ol>li:last-child {color: red;}			/* ol의 자식 중 마지막이 li라면 */
  ol>li:nth-child(4) {color: red;}	    /* ol의 자식 중 4번째가 li라면 */
  ul>:nth-last-child(2n+1) {color: red;}  /* ul의 자식 중 뒤에서부터 홀수번째 element */
  ul>:nth-last-child(2n) {color: red;}    /* ul의 자식 중 뒤에서부터 짝수번째 element */
  ```



* sibling element

  ```css
  p:first-of-type {color: red;}  		 /* 형제 중 첫번째로 등장하는 p tag */
  p:last-of-type {color: red;}  		 /* 형제 중 마지막으로 등장하는 p tag */
  p:nth-of-type(2) {color: red;}       /* 형제 중 두번째로 등장하는 p tag */
  p:nth-last-of-type(2) {color: red;}  /* 형제 중 뒤에서 두번째로 등장하는 p tag */
  ```



#### (H) Pseudo selector : Element

```css
p::first-letter {color: red;}    /* p tag의 첫글자 */
p::first-line {color: red;}      /* p tag의 첫 줄 */
h1::before {                     /* h1 element 앞에 */
    content: "before",
    color: red;
}  
h1::after {              		 /* h1 element 뒤에 */
    content: "after",
    color: red;
}  
::selection {color: red;}        /* drag할 때 선택되는 부분 */
```



### 02-03 Inline / Block

?



## 03. Bootstrap

### 03-01 Text

#### (A) Text alignment

* Basic text alignment

```html
<p class="text-justify">Basic aligned Text</p>
<p class="text-left">Left aligned Text</p>
<p class="text-center">Center aligned Text</p>
<p class="text-right">Right aligned Text</p>
```



* Text alignment on viewport size

```html
<p class="text-sm-left">Left aligned Text on viewports sized SM</p>
<p class="text-md-left">Left aligned Text on viewports sized MD</p>
<p class="text-lg-left">Left aligned Text on viewports sized LG</p>
<p class="text-xl-left">Left aligned Text on viewports sized XL</p>
```



#### (B) Text wrapping and overflow

* HTML에서 줄바꿈을 주는 방법

  * `<br>` : line break를 의미하며 이후 content는 new line에서 시작한다

  * `<p>` : 보통 줄바꿈은 새로운 문단이 시작할 때 사용하므로 새로운 paragraph를 만들면 줄이 바뀐다

  * `Text wrapping` : block level element은 기본적으로 text wrapping 효과를 가지고 있기 때문에 줄바꿈 을 할 수 있다

    * Text wrapping (default)

      ```html
      <div class="text-wrap">
          This text should not overflow the parent, instead line break
      </div>
      <!-- 기본적으로 text의 content는 parent element의 width를 넘어가면 줄바꿈 -->
      ```

    * No text wrapping

      ```html
      <div class="text-nowrap">
          This text should overflow the parent
      </div>
      <!-- text-nowrap을 주면 text의 content는 parent element의 width를 넘어서 계속 진행 -->
      ```

      

* Text truncate (only for block or inline-block element)

  * Block level element

    ```html
    <div class="text-truncate">
        parent element의 width를 넘은 content는 ...으로 표시
    </div>
    ```

  * Inline level element

    ```html
    <span class="d-inline-block text-truncate">
    	parent element의 width를 넘은 content는 ...으로 표시
    </span>
    <!-- span은 inline element이기 때문에 inline-block 필요-->
    ```

    

#### (C) Text transform

```html
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">CapiTaliZed text.</p>
```



#### (D) Font weight & Italics

```html
<p class="font-weight-bold">Bold text.</p>
<p class="font-weight-normal">Normal weight text.</p>
<p class="font-weight-light">Light weight text.</p>
<p class="font-italic">Italic text.</p>
```



### 03-02 Color

```html
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>
<p class="text-warning">.text-warning</p>
<p class="text-info">.text-info</p>
<p class="text-light bg-dark">.text-light</p>
<p class="text-dark">.text-dark</p> 
<p class="text-muted">.text-muted</p> ───────────┐ no link styling
<p class="text-white bg-dark">.text-white</p> ───┘
```

![result](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388418369.png)



#### (B) Text Background color

```html
<!-- 글자색은 .text-*를 통해 적용 -->
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>
<div class="p-3 mb-2 bg-light text-dark">.bg-light</div>
<div class="p-3 mb-2 bg-dark text-white">.bg-dark</div>
<div class="p-3 mb-2 bg-white text-dark">.bg-white</div>
```



#### (C) Background gradient

* `$enable-gradients: false` 가 default이기 때문에 사용 불가

* `$enable-gradients: true` 로 설정한다면 사용 가능

  ```html
  <div class="p-3 mb-2 bg-gradient-primary text-white">.bg-gradient-primary</div>
  <div class="p-3 mb-2 bg-gradient-success text-white">.bg-gradient-success</div>
  <div class="p-3 mb-2 bg-gradient-light text-dark">.bg-gradient-light</div>
  <div class="p-3 mb-2 bg-gradient-dark text-white">.bg-gradient-dark</div>
  ```

  

###  03-03 Spacing

#### (A) Basic class format

* for viewport size `xs` :  {property}{sides}-{size}

* for viewport size `sm`, `md`, `lg`, `xl` : {property}{sides}-{breakpoint}-{size}

* example

  ```css
  .mt-0 {
    margin-top: 0 !important;
  }
  
  .px-2 {
    padding-left: ($spacer * .5) !important;
    padding-right: ($spacer * .5) !important;
  }
  ```

  

#### (B) Property, Sides, Size

* Abbr for Property

  | Abbr | Property |
  | ---- | -------- |
  | m    | margin   |
  | p    | padding  |



* Abbr for Sides

  | Abbr  | Sides               |
  | ----- | ------------------- |
  | t     | top                 |
  | b     | bottom              |
  | l     | left                |
  | r     | right               |
  | x     | both left and right |
  | y     | both top and bottom |
  | blank | all direction       |



* Abbr for Size

  | Abbr | Size          |
  | ---- | ------------- |
  | 0    | 0             |
  | 1    | $spacer * .25 |
  | 2    | $spacer * .5  |
  | 3    | $spacer       |
  | 4    | $spacer * 1.5 |
  | 5    | $spacer * 3   |
  | auto | auto          |



### 03-04 Component

#### (A) Alert

```html
<div class="alert alert-primary" role="alert">
  This is a primary alert—check it out!
</div>
```

![1550388832816](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388832816.png)



#### (B) Badge

```html
<span class="badge badge-primary">Primary</span>
```

![1550388862411](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388862411.png)



#### (C) Button

```html
<button type="button" class="btn btn-primary">Primary</button>
```

![1550388883163](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388883163.png)



#### (D) Card

```html
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="..." alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

![1550388795649](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388795649.png)



#### (E) Carousel

```html
<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="..." alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="..." alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="..." alt="Third slide">
    </div>
  </div>
</div>
```

![1550388926364](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388926364.png)



#### (F) Dropdowns

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown button
  </button>
  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>
```

![1550388955793](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550388955793.png)



#### (G) Form

```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

![1550389020236](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550389020236.png)



#### (H) Modal

```html
<div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
```

![1550389065777](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550389065777.png)



#### (I) Nav & Navbar

```html
<ul class="nav">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```

![1550389107494](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550389107494.png)



#### (J) Pagination

```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```

![1550389135675](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\1550389135675.png)



### 03-05 Flex

#### (A) Flex in CSS

[FLEXBOX FROGGY]: http://flexboxfroggy.com/#ko

* flex 방향으로 정렬하기 (justify-content)

  ```css
  #flex {
      display: flex;
      justify-content: flex-start; 			/* conetent를 start부터 정렬  */
      justify-content: flex-end; 			    /* conetent를 end부터 정렬  */
      justify-content: center;	 			/* 수평 가운데 정렬  */
      justify-content: space-between; 		/* content 사이에 넓은 간격  */
      justify-content: space-around; 			/* content 사이에 좁은 간격  */
  }
  ```



* flex방향과 수직으로 정렬하기 (align-items)

  ```css
  #flex {
      display: flex;
      align-items: flex-start;        /* conetent를 start부터 정렬  */
      align-items: flex-end;		    /* conetent를 end부터 정렬  */
      align-items: center;			/* 수직 가운데 정렬  */
      align-items: baseline;			/* container 시작 위치에 정렬  */
      align-items: stretch;			/* container에 맞게 늘리기  */
  }
  ```



* 방향 설정하기 (flex-direction)

  ```css
  #flex {
      display: flex;
      flex-direction: row;        	    /* content 방향과 동일하게 정렬  */
      flex-direction: row-reverse;	    /* content 방향과 반대로 정렬  */
      flex-direction: column;				/* content를 위에서 아래로 정렬  */
      flex-direction: column-reverse;		/* content를 아래에서 위로 정렬 */
  }
  ```



* 순서 설정하기 (order)

  ```css
  #flex {
      display:flex;
  }
  
  .object {
      order: <integer>				/* object의 default order: 0  */
  }
  ```

  

#### (B) Flex in Bootstrap

[Bootstrap docs about Flex]: https://getbootstrap.com/docs/4.0/utilities/flex/

* `display: flex` 선언하기

  * flex box

    ```html
    <div class="d-flex p-2">This is a flexbox container!</div>
    ```

  * inline flex box

    ```html
    <div class="d-inline-flex p-2">This is a flexbox container!</div>
    ```



* Direction

  * Direction: Row

    ```html
    <div class="d-flex flex-row"></div>
    <div class="d-flex flex-row-reverse"></div>    
    ```

  * Direction: Column

    ```html
    <div class="d-flex flex-column"></div>
    <div class="d-flex flex-column-reverse"></div>
    ```



* Justify content (flex 방향으로 정렬하기)

  ```html
  <div class="d-flex justify-content-start">...</div>
  <div class="d-flex justify-content-end">...</div>
  <div class="d-flex justify-content-center">...</div>
  <div class="d-flex justify-content-between">...</div>
  <div class="d-flex justify-content-around">...</div>
  ```



* Align items (flex 방향과 수직으로 정렬하기)

  ```html
  <div class="d-flex align-items-start">...</div>
  <div class="d-flex align-items-end">...</div>
  <div class="d-flex align-items-center">...</div>
  <div class="d-flex align-items-baseline">...</div>
  <div class="d-flex align-items-stretch">...</div>  <!--start부터 end까지 영역 차지-->
  ```





