from PIL import Image

from application.common.exceptions import ImageProcessingError
from application.model import MediaURI
from . import ProcessorService


class ImageProcessorService(ProcessorService):
    """
    Handle the thumbnail extraction of any passed image
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
        Extract thumbnail, save in storage and returns the URI of the thumb and the image
        :param media:
        :return: a MediaURI object containing the URI of the thumbnail and the image
        :rtype: application.data.MediaURI
        :raise ImageProcessingError: means the image could not be processed by PIL
        """
        raise NotImplementedError()
