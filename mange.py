'''
author:yu
time:5-9
'''
from flask import Flask


app = Flask(__name__)
app.config.from_object('config') #模块的路劲
print(app.config['DEBUG'])



#http请求
#重定向
@app.route('/hello')
def hello():
    #status  code 200,404,301
    #content-type http headers
    #content-type = text/html
    return "<html> </html>"


#入口文件
#生产环境 ngix+uswgi
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
