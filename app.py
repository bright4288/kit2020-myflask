from flask import Flask, request, render_template, redirect, url_for, abort, session

app = Flask(__name__)


import game
import json

import dbdb

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html',data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/game.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['house'])
    return "{} 이 {} 을 골랐습니다.".format(character["name"],character["house"][0])


@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        #with open("static/game.txt", "r", encoding='utf-8') as f:
            #data = f.read()
            #character = json.loads(data)
            #print(character['house'])
        return "로딩중 , 이상한 세계 1에 오신 것을 환영합니다."
        #  "{} 이 {} 을 골랐습니다.".format(character["name"],character["house"][0])
    elif num == 2:
        return "로딩 실패, 처음으로 돌아가세요"
    elif num ==3:
        return "퉁퉁이"
    else:
        return "없어요"
    #return 'Hello, {}!'.format(name)

app.secreat_key = b'aaa!111/'



# # 로그아웃(session 제거)
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('form'))

# # 로그인 사용자만 접근 가능으로 만들면
# @app.route('/form')
# def form():
#     if 'user' in session:
#         return render_template('test.html')
#     return redirect(url_for('login'))

@app.route('/getinfo')
def getinfo():
    ret =  dbdb.select_all()
    print(ret[3])
    return render_template("getinfo.html", data=ret)
    # return'번호 : {}, 이름 : {}'.format(ret[0], ret[1])

@app.route('/naver')
def never():
    return redirect("https://www.naver.com/")
    #return render_template("naver.html")

@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")
 
@app.route('/urltest')
def url_test():
    return redirect(url_for('naver'))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_fount(error):
    return "페이지가 없습니다. URL를 확인 하세요",404

@app.route('/img')
def img():
    return render_template("image.html")


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
	app.debug = True
