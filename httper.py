
from urllib import request
import requests
class HTTPer:
    def get(self,url,return_json=True):
        r = request.get(url)
        #restful
        #json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.txt
