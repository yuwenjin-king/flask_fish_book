'''
author:yu
time:5-9
'''
from flask import Flask,make_response
from help import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config') #模块的路劲
print(app.config['DEBUG'])



#http请求
#重定向
@app.route('/book/searh/<q>/<page>')
def search(q,page):
    '''

    :param q:
    :param page:
    :return:
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == "isbn":
        result = YuShuBook.searcn_by_isbn
    else:
        result = YuShuBook.search_by_kewordp
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
