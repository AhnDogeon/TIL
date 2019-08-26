# JavaScript, Vue 내용 정리

## Ⅰ. JavaScript 

### 0. 시작

```html
<!DOCTYPE html>
<html lang="en">
<head...>
<body>
	<script>
		// 이 부분에 JavaScript 코드를 적어야 한다.
    </script>
</body>
</html>
```



### 1. 변수·상수 선언

> 선언은 변수, 상수, 함수를 처음 할당할 때만 사용한다. 
>
> 변수 : 미래에 재할당하거나 변할 것이 확실하다면 변수로 선언하도록 한다.
>
> 상수 : 미래에 재할당하지 않을 것이 확실하다면 상수로 선언하도록 한다.
>
> 재할당 하는 것과 할당한 상수 또는 변수의 값이 변화하는 것과는 상관이 없다.
>
> 변수, 상수, 함수의 이름짓는 방법은 다음 3가지가 있다.
>
> JS는 2번째 Lower Camel Case를 보통 사용한다, 
>
> ```
> Upper Camel Case = PostModelForm (시작과 띄어쓰기에서 대문자)
> Lower Camel Case = firstName, lastName (띄어쓰기에서 대문자, convention)
> Snake Case = this_is_python_variable (언더바 사용)
> ```

* ES5 (예전 스크립트 언어, 현재도 사용됨)

  변수, 상수 구분 없이 `var`로 선언한다. `ex : var number = 1` 

* ES6+ (최근 스크립트 언어)

  변수는 `let` 상수는 `const`로 선언한다. 

  ```js
  let string = 'hi';
  string = 'hello';
  const number = 1;
  ```



### 2. 기초 문법

* <u>문자열</u>

  문자열을 나타낼 때는 `작은따옴표('')` 또는 `큰따옴표("")`를 사용한다.

    단, 문자열 내에 상수, 변수가 존재할 시에는 `백틱(``)`으로 감싸준 후 그 안에 	`${변수이름}`을 넣어준다. 

  ```js
  const userName = prompt("who are you");
  const message = `<h1>hello ${userName}</h1>`;
  document.write(message);
  ```

  

* <u>배열</u>

  ```js
    const numbers = [1, 2, 3, 4];
    numbers[0]; // 1
    numbers[-1]; // undefined(모르겠는데요라는 뜻)
    numbers.length; // 4
  
    /* 원본이 달라지는 method */
    numbers.reverse(); // [4, 3, 2, 1]
    numbers.push("a"); // [4, 3, 2, 1, "a"]
    numbers.pop(); // [4, 3, 2, 1]
    numbers.unshift("a"); // ["a", 4, 3, 2, 1]
    numbers.shift(); // [4, 3, 2, 1]
  
    /* 복사본을 return 하는 method */
    numbers.includes(1); // true
    numbers.includes(0); // false
    numbers.push("a", "a"); // [4, 3, 2, 1, "a", "a"]
    numbers.indexOf("a"); // 4 : 가장 앞의 것
    numbers.indexOf("b"); // -1 : 없음
  
    numbers.join(""); // "4321aa"
    numbers.join(); // "4,3,2,1,a,a"
  ```

  

* <u>숫자</u>

  ```js
  100/0 // infinity
  -100/0 // -infinity
  100 - "1" // NaN(Not a Number) 
  1 == true //true
  1 === true // false 
  // 위와 같이 등호가 2개일 때는 예상치 못한 값이 나올 수도 있으므로 등호 3개를 사용하도록 한다
  ```




* <u>조건문</u>

  ```js
  if (조건1) {
  		실행문1
      } else if (조건2) {
          실행문2
      } else {
          실행문3
      }
  ```

  ※ 할당, 출력에는  `세미콜론(;)`을 붙였던 것과 달리 조건문, 반복문 중괄호 뒤에는 
       세미콜론을 붙이지 않는다.

  ※ 조건 설정할 때 등호는 파이썬 때와는 다르게, 3개 사용하도록 한다. `ex : userName === "1q2w3e4r"`

  

* <u>반복문</u>

  ```js
  // while loop
  let i = 0;
  while (i < 10) {
      console.log(i);
      i ++ ;
  }
  
  // for loop
  const numbers = [1, 2, 3, 4, 5];
  let sum = 0;
  for (let i = 0; i < numbers.length; i ++ ) {
      sum += numbers[i];
  }
  console.log(sum);
  
  sum = 0;
  for (const number of numbers) {		// 배열 뿐만 아니라 문자열에서도 of 사용이 가능하다.
      sum += number;
  }
  console.log(sum);
  ```

  

* 연산자

  ```js
  let c = 10
  c += 1  // 11
  c -= 1  // 10
  c *= 2 // 20
  c /= 2 // 10
  c ++; // 11
  c --; // 10
  ```
  
  

* <u>IMPORT</u>
  

	```html
	<body>
	<script src="./number.js">
</script>
	</body>
	```
	
	

* <u>함수</u>

  일반적인 함수의 형태는 다음 꼴과 같다.

  ```js
  function add (num1, num2) {
      return num1 + num2;
      
  function sqaure (num) {
      return num**2;   
  ```

  이를 간단하게 표현하는 형태는 다음과 같다.

  ```js
  let add = (num1, num2) {
      return num1 + num2;
  };
  let square = (num) { return num**2};
  // 인자가 하나이면 괄호가 생략가능하며, return문이 한줄이라면 return 키워드와 중괄호가 삭제 가능
  // 만약에 중괄호를 사용했다면 반드시 return을 써야한다.
  add = (num1, num2) => { return num1+num2;}
  square = num => num**2
  ```

  함수를 만들 때, 변수 또는 상수로 할당하고 이름을 지으면 선언적함수, 아니면 익명함수이다.

  ```js
  (name="ssafy") => `hi ${name}`;  //익명함수
  ((name="ssafy") => `hi ${name}`)("하이") // 익명함수의 실행 방법
  ```

  JS에는 인자 자리에 들어가는 함수를 callback 함수라고 부른다.

  ```js
  const numbersEach = (numbers, callback) => {
      let acc;  // JS 에서는 변수를 선언만 하는 것도 가능하다.
      for (const number of numbers) {
          acc = callback(number, acc)
      }
     	return acc
  }
  
  const multiplication (num, sum=1) => sum*num;
  numbersEach([1, 2, 3, 4, 5], multiplication);
  // 위 결과는 numbersEach([1, 2, 3, 4, 5], (num, sum=1) => sum*num ); 와 같다.
  ```

  함수에서 Object를 return할 때 인자와 Key 이름이 같다면 생략할 수 있다.

  ```js
  function makeArticle (id, title, content) {
  	return {
  		id,
  		title,
  		content,
  		makeOne() {
  			return `${this.id} 번 글: ${this.title} => ${this.content}`
  		}
  	}
  }
  
  console.log(makeArticle(1, "첫번째글", "안녕하세요. 반갑습니다.").makeOne()) 
  // "1 번 글: 첫번째글 => 안녕하세요. 반갑습니다." 
  // 파이썬과 동일하게 함수를 실행시킬땐, 괄호를 열고 닫는다.
  ```

  

* <u>Object</u>

  Python에서 dictionary라고 부르는 객체를  JS에서는 object라고 부른다.

  ```js
  const myObject = {
  	name : "KIM CHUL SOO",
      "favorite foods" : {
          Korean : "bulgogi",
          Japanese : "None",
      },
      intro : function () {  
          // 이때 만약 function을 빼먹는다면 this binding이 제대로 작동하지 않는다.(화살표함수)
          return `Hi, My name is ${this.name} `
      }, 
  	wait : function () {
          setTimeout ( () => {			// setTimeout은 JS에서 사용할 수 있는 함수
              console.log(this["favorite foods"].Korean)
          }, 1000 ) 	// 시간설정에서 단위는 ms이다. 1000ms = 1sec
      },
  };
  console.log(myObject.name); // "KIM CHUL SOO"
  console.log(myObject["favorite foods"].Korean); // "bulgogi"
  console.log(myObject.intro()); // "Hi, My name is KIM CHUL SOO" 화살표함수의 경우, "Hi, My name is undefined"가 출력
  console.log(myObject.wait()); // undefined 가 출력되고 1초 뒤 "bulgogi" 가 출력된다.
  myObject.wait(); // 1초뒤 "bulgogi"가 출력된다.
  ```

  

* Rest Spread

  **Rest 파라미터** 구문은 정해지지 않은 수(an indefinite number, 부정수) 인수를 배열로 나타낼 수 있게  해준다.

  ```js
  function addAll(...numbers) {
      let sum = 0;
      for (const number of numbers) {
          sum += number;
      }
      return sum;
  }
  
  console.log(addAll(1,2,3,4,5)); // 15
  ```

  **Spread 구문**을 사용하면 배열이나 문자열과 같이 반복 가능한 문자를 0개 이상의 인수 (함수로 호출할 경우) 또는 요소 (배열 리터럴의 경우)로 확장하여, 0개 이상의 키-값의 쌍으로 객체로 확장시킬 수 있다.

  ```js
  const a1 = [1, 2, 3, 4];
  const a2 = [5, 6, 7, 8];
  // [1, 2, 3, 4, 5, 6, 7, 8] 을 만들고 싶을 때, a1+a2를 하면 '1,2,3,45,6,7,8'로 된다.
  // const a3 = [...a1, ...a2]하면 원하는 배열을 만들 수 있다,
  function combine(numbers1, numbers2) {
      return [...numbers1, ...numbers2]
  }
  
  console.log(combine(a1, a2)) // [ 1, 2, 3, 4, 5, 6, 7, 8 ]
  
  function first0last100(numbers) {
      return [0, ...numbers ,100]
  }
  
  console.log(first0last100(a1)) // [ 0, 1, 2, 3, 4, 100 ]
  ```

  

* <u>Type</u>

  typeof 함수로 실행한다.

  ```js
  typeof 1; // "number"
  typeof (typeof 1); // "string"
  typeof (() => {}); // "function"
  typeof (function () {});  //"function"
  typeof (NaN); // "number"
  typeof infinity; // "number"
  typeof 100/0; // "NaN" (number)
  typeof -100/0; // "NaN" (number)
  typeof ("123" + 1);  // "string" "1231"
  typeof ("123"-1); // "number" 122
  typeof ("123"*2); // "number" 나누기도 같다,
  typeof undefined; // "undefined"
  typeof null; // "object"
  typeof []; // "object"
  typeof {}; // "object"
  ```

  

### 3.  HelperMethods

* <u>filter</u>

  **filter()** 메서드는 주어진 판별 함수를 통과하는 요소를 모아 새로운 배열로 만들어 반환합니다.

  ```js
  const products = [
      {name: "cucumber", type:"vegetable",},
      {name: "banana", type:"fruit",},
      {name: "carrot", type:"vegetable",},
      {name: "tomato", type:"fruit",},
  ];
  
  console.log(products.filter(product => product.type === "vege"));
  // [ { name: 'cucumber', type: 'vege' }, { name: 'carrot', type: 'vege' } ]
  console.log(products.filter(product => product.type === "vegetable").map(res => res.name));
  // ['cucumber', 'carrot' ]
  ```



* <u>find</u>

  **find()** 메서드는 주어진 판별 함수를 만족하는 **첫 번째 요소**의 **값**을 반환합니다. 그런 요소가 없다면 undeined를 반환합니다.

  ```js
  const avengers = [
      {name: "tony", id:1},
      {name: "captain", id:2},
      {name: "hulk", id:3},
      {name: "hulk", id:4},
  ];
  
  const a = avengers.find(avenger => avenger.name === "hulk" );
  console.log(a.id); //3
  ```

  

* <u>forEach</u>

  **forEach()** 메서드는 주어진 함수를 배열 요소 각각에 대해 실행합니다.

  ```js
  const colors = ["red", "blue", "green"];
  colors.forEach(color => {
      console.log(color);
  });
  // red
  // blue
  // green
  ```

  

* <u>map</u>

  **map()**메서드는 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환합니다.

  ```js
  const array1 = [1, 4, 9, 16];
  const map1 = array1.map(x => x * 2);
  console.log(map1);
  // [2, 8, 18, 32] 
  ```

  

### 4. fetch

ES6+이상에서 사용가능하다. 브라우저 에서만 사용가능하므로 `F12`를 눌러 나오는 콘솔에서 실행시켜야한다.
네트워크 통신을 포함한 리소스 취득이 필요할 때 사용하며 일반적인 오브젝트로 [`Request`](https://developer.mozilla.org/ko/docs/Web/API/Request) 와 [`Response`](https://developer.mozilla.org/ko/docs/Web/API/Response)가 포함되어 있다고 한다.

```js
// 기본적인 형태
// (만들고), 정보를 담고, 보내고, 기다리고, 처리한다.
fetch(URL) // 만들고, 정보를 담고, 보내고
    .then(response => response.json()) // 기다리고, 도착한 데이터를 파싱함
    .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.


// 예시 1
const DOMAIN = "https://jsonplaceholder.typicode.com/";
const RESOURCE = "posts";
const QUERY_STRING = "";
const URL = DOMAIN + RESOURCE + QUERY_STRING;
const getRequest = URL => {
    fetch(URL) // 만들고, 정보를 담고, 보내고
        .then(response => response.json()) // 기다리고, 도착한 데이터를 파싱함
        .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.
    	.catch( e => console.log(e.message))
};

getRequest(URL);

// 예시 2
const postRequest = URL => {
    fetch(URL, {
        method: "post",
        body: JSON.stringify({title: "new post", content: "new content", userId: 1}),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    }) // 만들고, 정보를 담고, 보내고
        .then(response => response.json()) // 기다리고, 도착한 데이터를 파싱함
        .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.
};

postRequest(URL);
```



### 5. XHR

[`XMLHttpRequest`](https://developer.mozilla.org/ko/docs/Web/API/XMLHttpRequest) (XHR) 은 [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) 요청을 생성하는 [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript) [API](https://developer.mozilla.org/en-US/docs/Glossary/API) 입니다. 이것의 메소드는 [browser](https://developer.mozilla.org/en-US/docs/Glossary/browser)와 [server](https://developer.mozilla.org/en-US/docs/Glossary/server)간의 네트워크 요청을 전송하도록 해줍니다.

```js
//XHR은 브라우저에서만 실행시킬 수 있다. console 에 복붙 한뒤에 실행시키면 된다.
const DOMAIN = "https://jsonplaceholder.typicode.com/";
const RESOURCE = "posts";
const QUERY_STRING = "";
const URL = DOMAIN + RESOURCE + QUERY_STRING;

// request 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();

// XHR 요청 발사 준비 (method, url)
// 요청을 만들고, 정보를 담고, 보내고, 기다리고, 처리한다.
XHR.open("POST", URL);

XHR.setRequestHeader(
    "Content-Type",
    "application/json;charset=UTF-8"
)

// POST 요청을 보낼 때 괄호 안에 BODY (JSON : string )를 넣는다
XHR.send(
    JSON.stringify({ "title":"NewPost", "body":"This is New Post", "userId":1  })
    // '{ "title":"NewPost", "body":"This is New Post", "userId":1}'를 보내게 된다.
);

XHR.addEventListener("load", e => {
   const parseData = JSON.parse(e.target.response);
   console.log(parseData);
  // 오브젝트 형태로 콘솔에 출력하게 된다.
});
```



### 6. axios

`base.html`

```html
// axios를 사용하기 위해서 아래의 줄을 꼭 써줘야 한다.
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    function getCookies() {
        const cookieSet = {};
        document.cookie.split('; ').forEach(cookieString => {
            const kv = cookieString.split('=');
            cookieSet[kv[0]] = kv[1];
        });
        return cookieSet
    }
    const likeButtons = document.querySelectorAll('.like-button');
    getCookies().csrftoken
    likeButtons.forEach(button => {
        button.addEventListener('click', e => {
            const postId = button.dataset.id;
            const URL = `/insta/${postId}/like/`; // toggle_like 함수의 URL 
            axios.get(URL)
                .then(response => {
                    const likeCountArea = document.querySelector(`#like-count-${postId}`);
                    console.log(response);
                    likeCountArea.innerHTML = response.data.likeCount;
                    console.log(button.innerHTML);
                })
        })
    })
</script>
```

`views.py`

```python
from django.http import JsonResponse

@login_required()
@require_POST
def toggle_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    # if post.like_users.filter(id=user.id).exists():  # 찾으면, [value] / 없으면, []
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return JsonResponse({'likeCount': post.like_users.count()})
```



### 7. 기타 Methods

| 메소드                       | 사용 예시                                                    |
| ---------------------------- | ------------------------------------------------------------ |
| **alert()**                  | `alert('Welcome to JS');`                                    |
| **confirm()**                | `confirm('공부를 합시다.');`                                 |
| **document.write()**         | `document.write('<h1>Happy Hacking!</h1>')`                  |
| **document.querySelector()** | `const title = document.querySelector('h1').innerText;<br `/><br />`document.querySelector('h1').innerText = 'Goodbye World!';` |
| **console.log()**            | `const greeting = "hello"; console.log(greeting);`           |
| **prompt()**                 | `const userName = prompt("who are you");`                    |
| **JSON.stringify()**         | `JSON.stringify({ "title":"NewPost", "body":"This is New Post", "userId":1  })` |
| **JSON.parse()**             | `XHR.addEventListener("load", e => { const parseData = JSON.parse(e.target.response); console.log(parseData);` |



## Ⅱ. Vue.js 

수업 듣고 각자 추가해보면 될거 같아요~ ㅠㅠ



## Ⅲ. 추가 용어 설명

* `JavaScript` : 자바스크립트는 객체 기반의 스크립트 프로그래밍 언어이다. 이 언어는 웹 브라우저 내에서 주로 사용하며, 다른 응용 프로그램의 내장 객체에도 접근할 수 있는 기능을 가지고 있다.

* `Node.js` : Node.js는 확장성 있는 네트워크 애플리케이션(특히 서버 사이드) 개발에 사용되는 소프트웨어 플랫폼이다. 작성 언어로 자바스크립트를 활용한다. 크롬 V8 엔진 기반으로 만들어졌다.

* `DOM` : 문서 객체 모델(DOM; Document Object Model)은 객체 지향 모델로써 구조화된 문서를 표현하는 형식이다.

* `Vue.js` :  웹 개발을 단순화하고 정리하기 위해 개발된 대중적인 자바스크립트 프론트엔드 프레임워크이다.
  
  