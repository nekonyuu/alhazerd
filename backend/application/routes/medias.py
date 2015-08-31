from flask.ext.classy import FlaskView
from greplin import scales

from application.common.config import config
from application.backend.medias import MediasBackend

class MediasView(FlaskView):
    """
    Medias list view
    """

    client_errors = scales.IntStat('4xx')
    server_errors = scales.IntStat('5xx')
    latency = scales.PmfStat('latency')

    def __init__(self):
        super(MediasView, self).__init__()
        scales.init(self, '/api/medias')
        self._media_backend = MediasBackend(config)

    def index(self):
        return "MediaList", 200

    def get(self, media_id):
        return "MediaID: %s" % media_id, 200
