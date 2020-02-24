from app import app, mongo
from flask import render_template, jsonify

@app.route('/')
@app.route('/index')
def index():
    ques_list = mongo.db.quiz.find()
    # print('ques_list: ' + jsonify(ques_list))
    # print(render_template('index.html', ques_list=ques_list))
    return render_template('index.html', ques_list=ques_list)
    # return "Hello, World! to the Quiz app"