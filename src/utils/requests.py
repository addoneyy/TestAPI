import requests

class HttpRequest:

    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        """
            get
        """
        return self.session.request("get", url=url, **kwargs )

    def post(self, url, **kwargs):
        """
            post
        """
        return self.session.request("post", url=url, **kwargs )

    def request(self, url, **kwargs):
        """
            request
        """
        return self.session.request("request", url=url, **kwargs )

    def put(self, url, **kwargs):
        """
            put
        """
        return self.session.request("put", url=url, **kwargs )

    def __del__(self):
        """
            析构函数：释放对象
        """
        self.session.close()

http_request = HttpRequest()
