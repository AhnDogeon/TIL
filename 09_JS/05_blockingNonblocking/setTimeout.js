function sleep_3s() {
    setTimeout(() => {
        console.log('Wake Up!')
    }, 3000)
}

console.log('Start Sleeping');
sleep_3s();
console.log('End of Program');