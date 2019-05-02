function subAll(){}
function mulAll(){}

module.exports = {
    addAll(numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    subAll() {
        let total = 0;
        numbers.forEach( number => total -= number);
        return total;
    },
    mulAll() {
        let total = 1;
        numbers.forEach( number => total *= number);
        return total;
    },
    name: 'neo'
};

phoneNumber = '01012341234';

module.exports.phoneNumber = phoneNumber;