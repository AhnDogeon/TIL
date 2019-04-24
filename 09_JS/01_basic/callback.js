// 인자로 배열을 받는다. 해당 배열의 모든 요소를 더한 숫자를 return
const numbersEachAdd = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
};

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 뺀 숫자를 return
const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
};
// 인자로 배열을 받는다. 해당 배열의 모든 요소를 곱한 숫자를 return
const numberEachMul = numbers => {
    let acc= 1;
    for (const number of numbers) {
        acc *= number;
    }
    return acc;
};
//
// console.log(numbersEachAdd([1, 2, 3, 4, 5]));
// console.log(numbersEachSub([1, 2, 3, 4, 5]));
// console.log(numberEachMul([1, 2, 3]));


// 숫자로 이루어진 배열의 요소들을 각각 [???] 한다. [???]는 알아서 해라. (더한, 뺀, 곱, 나눗 등)
const numberEach = (numbers, callback) => {
    let acc; // js에서는 변수 선언만 할 수 있다.
    for (const num of numbers) {
        acc = callback(num, acc);
    }
    return acc;
};

// 최종적으로 이렇게 쓰려고 함, 밑에는 이해 위한 것
console.log(numberEach([1,2,3,4,5], (number, sum=0) => sum += number));
numberEach([1, 2, 3, 4, 5], (number, acc=1) => acc *= number);

const muler = (number, sum=1) => {
    return sum *= number
};

numberEach([1, 2, 3, 4, 5], muler);

const adder = (number, sum=0) => {
    return sum += number
};

numberEach([1, 2, 3, 4, 5], adder);