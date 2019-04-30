function hi () {

}

const bye = () => {

};

const me = {
    name: 'Ahn Do Geon',
    phone: '01012345678',
    email: 'aaa@aaa.com',
    intro: function () {
        return `Hi my name is ${this.name}.`
    }
};
console.log(me.intro());

const you = {
    name: 'dogeon',
    phone: '01012345678',
    email: 'aaa@aaa.com',
    intro:  () => {
        return `Hi my name is ${this.name}.`
    },

    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    },
};

console.log(you.intro());
console.log(you.wait());

// 결론 : key value로 사용 할 때는 애로우function 안쓰고 일반 함수 정의로 사용한다.