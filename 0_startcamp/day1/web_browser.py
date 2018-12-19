import webbrowser # 사용하는 구문보다 무조건 앞에 있어야 함

keywords = [
    '사당 맛집',
    '영화 순위',
    '옷'
]#검색하고 싶은 것을 넣는다

for keyword in keywords: #콜론이 있으면 들여쓰기
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)

