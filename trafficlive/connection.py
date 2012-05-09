import requests
from trafficlive.urlconf import urls


def test_func(cls, *args, **kwargs):
    result = cls._send_request(url, method, **kwargs)


class _Connection(type):
    def __new__(cls, clsname, clsbases, clsdict):
        t = type.__new__(cls, clsname, clsbases, clsdict)
        for key, value in urls.iteritems():
            print key, ';', value 
            url = value.pop('url')
            print url
            method = value.pop('method')
            print method
            setattr(cls, key, test_func)
            print "Set attr"
        return t

    def _send_request(cls, *args, **kwargs):
        pass


class Connection(object):
    __metaclass__ = _Connection

    def __init__(self, host="https://api.sohnar.com/TrafficLiteServer/openapi", username=None, password=None):
        self.conn = requests.session()
        self.host = host

    def _send_request(self, url, method):
        func = getattr(self.conn, method)
        func("%s%s" % (self.host, url), auth=(self.username, self.password))

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def set_host(self, host):
        self.host = host

