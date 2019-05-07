typeof 1; // number가 나온다
typeof (typeof 1); // string

typeof (() => {}) // function
typeof (function() {}) // function
typeof (NaN) // number : NaN은 숫자가 아니지만 숫자 관련된 연산으로 나오는 결과. 때문에 number가 나온다.

typeof undefined // undefined 타입
typeof null // object

