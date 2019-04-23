const me = {
    name: 'AhnDoGeon',
    'phone number': '01012341234' // 띄어쓰기가 있으면, 'key': 로 쓴다.
    appleProducts: {
        ipad: '2018pro',
        iphone: '6s+',
        macbook: '2018 pro',
    }
};

me.name; // AhnDoGeon
me['name']; // AhnDoGeon
me['phone number']; // 01012341234
me.appleProducts; // {ipad: '2018Pro', ....}
me.appleProducts.ipad; // '2018pro'