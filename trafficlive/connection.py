import requests
from trafficlive.urlconf import urls


class _Connection(type):
    def __new__(cls, clsname, clsbases, clsdict):
        t = type.__new__(cls, clsname, clsbases, clsdict)

        def tfunc(cls, url, method, extra=None):
            if not extra:
                extra = {}
            def test_func(cls, extra): cls._send_request(url, method, extra)
            return test_func
            
        for key, value in urls.iteritems():
            url = value.pop('url')
            method = value.pop('method')
            func = tfunc(cls, url, method, value)
            setattr(t, key, func)
        return t

    def _send_request(cls, *args, **kwargs):
        pass


class Connection(object):
    __metaclass__ = _Connection

    def __init__(self, host="https://api.sohnar.com/TrafficLiteServer/openapi", username=None, password=None):
        self.conn = requests.session()
        self.host = host

    def _send_request(self, url, method, extra):
        full_url = url % extra
        func = getattr(self.conn, method.lower())
        response = func("%s%s" % (self.host, full_url), auth=(self.username, self.password))
        print response
        return response

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def set_host(self, host):
        self.host = host

