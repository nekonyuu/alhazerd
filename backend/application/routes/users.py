from flask.ext.classy import FlaskView, route
from greplin import scales

from application.common.config import config
from application.backend.users import UsersBackend


class RegisterView(FlaskView):
    """
    Handle signup
    """
    client_errors = scales.IntStat('4xx')
    server_errors = scales.IntStat('5xx')
    latency = scales.PmfStat('latency')

    def __init__(self):
        super(RegisterView, self).__init__()
        scales.init(self, '/api/register')

    def index(self):
        return "Register", 200


class ProfileView(FlaskView):
    """
    Shows personal profile
    """

    client_errors = scales.IntStat('4xx')
    server_errors = scales.IntStat('5xx')
    latency = scales.PmfStat('latency')

    def __init__(self):
        super(ProfileView, self).__init__()
        scales.init(self, '/api/profile')
        self._users_backend = UsersBackend(config)

    def index(self):
        return "MyProfile", 200


class UsersView(FlaskView):
    """
    Users list view
    """

    client_errors = scales.IntStat('4xx')
    server_errors = scales.IntStat('5xx')
    latency = scales.PmfStat('latency')

    def __init__(self):
        super(UsersView, self).__init__()
        scales.init(self, '/api/home')

    def index(self):
        return "UsersList", 200

    def get(self, user_id):
        return "UserID: %s" % user_id, 200
