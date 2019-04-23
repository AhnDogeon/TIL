// This is Comment

function concat(str1, str2) {
    return `${str1} - ${str2}`;
}


const concat = function (str1, str2) {
    return `${str1} - ${str2}`;
};

const concat = (str1, str2) => `${str1} - ${str2}`;

//=======================================================

const checkLongStr = string => {
    if (string.length > 10) {
        return true;
    } else {
        return false;
    }
};

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING');
} else {
    console.log('SHORT STRING');
}
const checkLongStr = string => string.length > 10;

checkLongStr(concat('Happy', 'Hacking')) ? console.log('LONG') : console.log('SHORT');

console.log(
    checkLongStr(concat('Happy', 'Hacking')) ? 'LONG' : 'SHORT'
);