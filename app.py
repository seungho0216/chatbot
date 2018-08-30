from flask import Flask
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
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
