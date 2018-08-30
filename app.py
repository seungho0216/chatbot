from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗 봇 페이지 입니다!!'
    
@app.route('/keyboard')
def keyboard():
    keyboard =  {
                  "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이", "영화"]
                }
    json.keyboard = json.dumps(keyboard)
    return json.keyboard
    
@app.route("/message", methods=["POST"])
def message():
    # content라는 key value를 msg에 저장
    msg = request.json["content"]
    
    # 카톡에서 명령어 입력시 text 에 있는 문구가 출력됨
    # 현재는 사용자가 말하는것을 그대로 답 하는 상태
    json_return = {
        "message": {
            "text":msg
            
        },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "고양이", "영화"]
            
        }
    }
    return jsonify(json_return)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
