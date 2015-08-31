from flask.ext.classy import FlaskView
from greplin import scales

from application.common.config import config
from application.backend.medias import MediasBackend
from application.processors.image import ImageProcessorService
from application.processors.video import VideoProcessorService

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
        self._image_processor = ImageProcessorService(config)
        self._video_processor = VideoProcessorService(config)

    def index(self):
        return "MediaList", 200

    def get(self, media_id):
        """
        Return the media passed in parameter
        :param media_id:
        :type media_id: str
        :return:
        """
        return "MediaID: %s" % media_id, 200

    def post(self, data):
        """
        Handle new media
        :param data: the media to save/handle
        :return:
        """
        raise NotImplementedError()

    def delete(self, media_id):
        """
        Delete the specified media from database and storage
        :param media_id:
        :type media_id: str
        :return:
        """