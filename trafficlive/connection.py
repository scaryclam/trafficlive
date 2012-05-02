import requests


class Connection(object):
    def __init__(self, host="https://api.sohnar.com/TrafficLiteServer/openapi", username=None, password=None):
        self.conn = requests.session()
        self.host = host

    def get_employees(self):
        url = "/staff/employee"
        self._send_request(self, url, "GET")

    def get_employee(self, employee_id):
        url = "/staff/employee/%s" % str(employee_id)
        self._send_request(self, url, "GET")

    def get_departments(self):
        url = "/staff/department"
        self._send_request(self, url, "GET")

    def get_department(self, dept_id):
        url = "/staff/department/%s" % str(dept_id)
        self._send_request(self, url, "GET")

    def get_locations(self):
        url = "/staff/location"
        self._send_request(self, url, "GET")

    def get_location(self, location_id):
        url = "/staff/location/%s" % str(location_id)
        self._send_request(self, url, "GET")

    def _send_request(self, url, method):
        func = getattr(self.conn, method)
        func("%s%s" % (self.host, url), auth=(self.username, self.password))

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def set_host(self, host):
        self.host = host

