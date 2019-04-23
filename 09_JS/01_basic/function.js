/*
    def func(arg1, arg2):
        ...
        return value

    func = lambda arg1, arg2: value
 */

// 1. 함수 키워드 정의
function add (num1, num2){
    return num1 + num2;
}

// 2. 변수에 함수 로직 할당 ***** 함수는 const ***** 여기서 테스트용으로 let으로 해둠
const sub = function (num1, num2) {
    return num1 - num2;
}; // = 으로 할당하면 세미콜론 써줘야 함


// 3. 함수 표현식 2가지
let mul = function (num1, num2) {
    return num1 * num2;
};

    /*
        step 1: function 키워드를 없앤다
        step 2: () 와 {} tkdldp => 를 넣는다.
     */
mul = (num1, num2) => {
    return num1 * num2
};

    /*
        추가 리팩토링
        step 1 : 인자가 단 하나라면, () 가 생략 가능하다.
        step 2 : 함수 블록 안에 코드가 return 문 한 줄이라면, {} & return 키워드 삭제 가능하다. 단, 둘 다 삭제하거나 둘 다 남기거나
     */

let square = function (num) {
    return num ** 2;
};

// arrow function 으로!
square = (num) => {
    return num ** 2;
};

// 리팩토링
square = num => num ** 2;

square(3); // 9

let noArgs = () => {
    return 'nothing';
};

noArgs = () => 'nothing';
noArgs =  => 'nothing';

oneArgs = a => 'one';
manyArgs = (a, b, c, d, e) => 'many';


/* Default Args */
function sayHello (name) {
    return `hi ${name}!`
}
//얘를 줄이려면!
const sayHello = function (name = 'ssafy') {
    return `hi ${name}!`;
}

const sayHello = (name = 'ssafy') => `hi ${name}!`;


sayHello(); // hi ssafy
sayHello('do geon'); // hi do geon

(num => num ** 2)(4); // 16 : 익명함수 실행시키기
