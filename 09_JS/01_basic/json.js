const myObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and Cream',
};

const jsonData = JSON.stringify(myObject);
jsonData // "{coffee: 'Americano', iceCream: 'Cookie and Cream'}"
console.log(typeof jsonData); // string

const parseData = JSON.parse(jsonData);
console.log(typeof parseData); // object