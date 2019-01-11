from flask import Flask, jsonify, request
import random
import requests
app = Flask(__name__)

@app.route('/') # 데코레이터, 주소 값이라 보면됨
def index(): # 도메인 뒤에 아무것도 없을 때 보통 인덱스 페이지라고 함
    return 'Hi!'


@app.route('/dictionary/<string:word>')
def word(word):
    data = {
        'apple' : '사과'
    }
    if word in data:
        return (f'{word} 은(는) {data[word]}')
    else:
        return (f'{word} 은(는) 나만의 단어장에 없는 단어')







@app.route('/ssafy')
def ssafy():
    return 'ssssssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return (f'hi {name}!')

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1,46), 6) 
    return jsonify(numbers)



if __name__ == '__main__':
    app.run(debug=True) # 서버야 일해라

