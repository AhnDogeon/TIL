// fetch.js ES6+ 에서 제공하는 기능, BROWSER 에서 실행

const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '';

const URL = DOMAIN + RESOURCE + QUERY_STRING;

// (만들고) => 정보를 담고 => 보내고 => 기다리고 => 처리한다.

const getRequest = (URL) => {
    fetch(URL) // 만들고 => 정보를 담고 => 보내고
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱함
        .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.
};

getRequest(URL);

const postRequest = URL => {
    fetch(URL, {
        method: 'POST',
        body: JSON.stringify({
            title:'new post',
            content: 'new content',
            userId: 1}),
        headers: {
            'Content' : 'application/json; charset=UTF-8'
        }
    }) // 위 만들고 => 정보를 담고 => 보내고까지 완료 post
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱함
        .then(parseData => console.log(parseData)); // 파싱한 데이터를 출력한다.
};
