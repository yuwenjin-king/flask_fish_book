'''
author:yu
time:5-9
'''
from flask import Flask,make_response


app = Flask(__name__)
app.config.from_object('config') #模块的路劲
print(app.config['DEBUG'])



#http请求
#重定向
@app.route('/hello')
def hello():
    #status  code 200,404,301
    #content-type http headers
    #content-type = text/html 默认值
    #response
    headers = {
        'content-type':'text/plain',
        'location':'http:'
    }
    response = make_response("<html> </html>")
    return "<html> </html>"
#http://t.yushu.im/v2/book/search?q=0&start=&count=0
#https://api.douban.com/v2/book
#入口文件 http://t.yushu.im/v2/book/isbn/{isbn}
#生产环境 ngix+uswgi



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
