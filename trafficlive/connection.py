import requests


class _Connection(type):
    def __new__(cls, clsname, clsbases, clsdict):
        t = type.__new__(cls, clsname, clsbases, clsdict)
        t.__foo__ = "Hello World"
        return t


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

