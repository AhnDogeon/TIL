function solveMe(...numbers) {
    var mid = new Array();
    for (let i = 1; i < numbers.length; i++) {
        mid.push(numbers[0] * numbers[i]);
    }
    console.log(mid);
    return mid;
}

const a = solveMe(2, 1, 2, 3, 4);
const b = solveMe(5, 10, 20);
console.log([...a, ...b]);