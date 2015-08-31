class ProcessorService(object):
    """
    Interface for processor service
    """
    def process(self, media):
        """
        Process the passed media and return URIs of processed data
        :param media: the media to process
        :return: a MediaURI object containing the URI of the thumbnail and the media
        :rtype: application.data.MediaURI
        """
        raise NotImplementedError()