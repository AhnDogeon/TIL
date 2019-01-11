from flask import Flask, jsonify, request
import random
import requests
app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def word(word):
    data = {
        'apple' : '사과'
    }
    if word in data:
        return (f'{word} 은(는) {data[word]}')
    else:
        return (f'{word} 은(는) 나만의 단어장에 없는 단어')


if __name__ == '__main__':
    app.run(debug=True) # 서버야 일해라

