#导入flask框架,小session设置状态保持session的k-v
from flask import Flask, render_template, session
import base64
import os
# 实现状态保持中的session信息的位置存储
from flask_session import Session
# 导入redis链接redis数据库
from redis import StrictRedis


app = Flask(__name__)

password = bytes.decode(base64.b64encode(os.urandom(48)))
# 配置信息
# 设置秘钥
app.config['SECRET_KEY'] = password
# 设置session有效期
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
# 指定存在redis数据库的实例
app.config['SESSION_REDIS'] = StrictRedis()
# 指定存储数据库的类型
app.config['SESSION_TYPE'] = 'redis'
# session信息是否签名
app.config['SESSION_USE_SIGNER'] = True


Session(app)


@app.route('/')
def indes():
    # 设置session
    session['itcast'] = '2018'
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='192.168.199.131', port=7890, debug=True)