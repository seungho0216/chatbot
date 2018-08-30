from flask import Flask, request, jsonify
import json
import os
import random

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
    
    if msg == "메뉴":
        menu = ["20층", "멀캠식당", "찹쌀탕수육", "급식"]
        return_msg = random.choice(menu)
    elif msg == "로또":
        numbers = list(range(1,46))
        pick = random.sample(numbers, 6)
        return_msg = str(sorted(pick))
    else:
        return_msg = "현재 메뉴만 지원합니다."
        
    
    # 카톡에서 명령어 입력시 text 에 있는 문구가 출력됨
    # 현재는 사용자가 말하는것을 그대로 답 하는 상태
    json_return = {
        "message": {
            "text":return_msg
            
        },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "고양이", "영화"]
            
        }
    }
    return jsonify(json_return)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
