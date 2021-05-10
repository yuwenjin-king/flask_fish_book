
from httper import HTTPer
class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count=()&start={}"
    @classmethod
    def searcn_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTPer.get(url)
        return result
    @classmethod
    def search_by_keword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTPer.get(url)
        return result
