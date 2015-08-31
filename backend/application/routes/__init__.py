from flask.ext.classy import FlaskView
from greplin import scales


class HomeView(FlaskView):
    """
    Home view
    """

    client_errors = scales.IntStat('4xx')
    server_errors = scales.IntStat('5xx')
    latency = scales.PmfStat('latency')

    route_base = '/'

    def __init__(self):
        super(HomeView, self).__init__()
        scales.init(self, '/api/home')

    def index(self):
        return "Homepage", 200
