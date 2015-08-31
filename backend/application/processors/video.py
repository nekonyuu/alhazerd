import av

from application.common.exceptions import VideoProcessingError
from application.model import MediaURI
from . import ProcessorService


class VideoProcessorService(ProcessorService):
    """
    Handle the thumbnail extraction of any passed video
    """

    def __init__(self, config):
        """
        :param config:
        :type config: application.common.tools.Map
        :return:
        """
        self._thumbs_path = config.storage.thumbnails_path
        self._storage_path = config.storage.medias_path

    def process(self, media):
        """
        Extract thumbnail, save in storage and returns the URI of the thumb and the video
        :param media:
        :return: a MediaURI object containing the URI of the thumbnail and the video
        :rtype: application.data.MediaURI
        :raise VideoProcessingError: means the video could not be processed by PyAV/ffmpeg
        """
        raise NotImplementedError()
