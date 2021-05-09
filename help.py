def is_isbn_or_key(q):
    '''
        q :关键字 isbn
        page
     '''
    #isbn isbn13
    #isbn10
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdight():
        isbn_or_key = 'isbn'
    short_q = q.replace('-','')
    if '-' in q and short_q.isdight() and len(short_q):
        isbn_or_key = 'isbn'
    return isbn_or_key