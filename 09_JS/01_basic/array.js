const numbers = [1, 2, 3, 4];

numbers[0]; // 1
numbers[-1]; // undefined
numbers.length; // 4

/*
    원본이 달라지는 methods
 */
numbers.reverse(); // [4, 3, 2, 1]
numbers; // [4, 3, 2, 1]
numbers.reverse(); // [1, 2, 3, 4]

numbers.push('a') // 5 : new length
numbers; // [1, 2, 3, 4, "a"]


numbers.pop(); // "a"
numbers; // [1, 2, 3, 4]

console.log(numbers.unshift('a')); // 5 : new length
numbers; // ["a", 1, 2, 3, 4]
numbers.shift(); // "a"
numbers; // [1, 2, 3, 4]

/*
    Copy 혹은 다른 결과 return
 */
numbers.includes(1); // true
numbers; // [1, 2, 3, 4]


numbers.includes(0); // false
numbers; // [1, 2, 3, 4]

numbers.push('a', 'a'); // test
numbers.indexOf('a'); // 4
numbers.indexOf('b'); // -1 => 없음

numbers; // [1, 2, 3, 4, 'a', 'a']
console.log(numbers.join('-')); //'1-2-3-4-a-a'
console.log(numbers.join('')); // '1234aa'
console.log(numbers.join()); // '1,2,3,4,a,a'

