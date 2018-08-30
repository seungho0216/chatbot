
     ,-----.               ,--.      ,--.,------.  ,------.
    '  .--./,--.,--. ,---. |  | .-,  |  ||  .-.  \ |  .---'
    |  `--, |  ||  || .-./ |  '' /   |  ||  |  \  :|  `--, 
    |  |    '  ''  '' '--. |  .. \   |  ||  '--'  /|  `---.
    `--'     `----'  `---' `--' `-'  `--'`-------' `------'
    -----------------------------------------------------------

# 파이썬 챗봇 만들기!

### 카카오톡 플러스친구 관리자센터

- 플러스 친구 생성 후 공개설정 해줄 것(공개안하면 검색 불가)
- 스마트 채팅 _> API형 사용

### c9 개발

- 우측 상단의 톱니바퀴에 들어가서 python3 로 설정 변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard
```py
from flask import Flask
# json으로 변환하기 위한 모듈
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗 봇 페이지 입니다!!'
    
@app.route('/keyboard')
def keyboard():
    # keyboard 딕셔너리 생성
    keyboard =  {
                  "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이", "영화"]
                }
    # 딕셔너리를 json 으로 바꿔서 리턴해주기 위한 코드
    json.keyboard = json.dumps(keyboard)
    return json.keyboard
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

```

- request
    - url : 어떤 경로로 보낼지?
    - method: 어떤 방법으로 보낼지?
    - parameter: 어떤 정보를 담을지?

- response
    - data type: 어떤 형식으로 답할지?
    - 
    - 