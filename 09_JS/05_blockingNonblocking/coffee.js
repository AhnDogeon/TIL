function makeCoffee(order, serve) {
    let cup;

    // Coffee 기계 밑에서 걸리는 시간
    setTimeout(() => {
        cup = order;
        serve(cup)
    }, 2000);
    return cup;
}

const myCoffee = makeCoffee('latte', console.log(myCoffee));