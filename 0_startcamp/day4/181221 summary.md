# 181221 수업정리

## 1. app.py 에서 로또 함수 만들어 url 통한 접근 가능하게 하기

* ```python
  from flask import Flask, jsonify, render_template # render_template : 파일을 보내주는 애 //templates 폴더 밑에 index.html 파일을 보내주는 것
  ## jsonify 는 이용자가 이용할 수 있게 
  from random import sample
  import requests
  
  
  
  app = Flask(__name__)
  
  @app.route('/ide/<string:username>/<string:workspace>') # 변수 설정, 사용자로부터 임의로 입력값을 받을 수 있다.
  def username_workspace(username,workspace):
      return "{}'s hot {}!".format(username, workspace)
  
  @app.route('/get_lotto/<int:draw_no>')
  def get_lotto(draw_no):
      url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
      url = url + str(draw_no)
      
      response = requests.get(url) 
      lotto_data = response.json()
      numbers = []
  
      for key, value in lotto_data.items():
          if 'drwtNo' in key:
              numbers.append(value)
      
      numbers.sort()
      bonus_number = lotto_data['bnusNo']
      final_dict = {
          'numbers' : numbers,
          'bonus' : bonus_number
      }
      return jsonify(final_dict)
      
  
  @app.route("/")
  def index():
      return render_template('index.html') # 템플릿으로만 찾으므로 templates라는 폴더로 무조건 만들어줘야 함
      
      
  @app.route("/hi")
  def hi():
      return 'Hello SSAFY'
      
  @app.route("/pick_lotto")
  def pick_lotto():
      return jsonify(sample(range(1,46), 6))
  
  # @app.route("/get_lotto")
  # def get_lotto():
  #     data = {
  #         'numbers' : [1,2,3,4,5,6],
  #         'bonus' : 7
  #     }
  #     return jsonify(data)
      
  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080) ## 이 구문은 무조건 맨 밑에 있어야 함
      # $ export FLASK_ENV='development' 저장과 동시에 서버 새로고침
      # $ flask run -h 0.0.0.0 -p 8080
      # $ python3 app.py 로 바로 실행 가능
  ```

* 