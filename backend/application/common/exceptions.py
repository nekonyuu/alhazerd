class MediaProcessingError(Exception):
    pass

class VideoProcessingError(MediaProcessingError):
    pass

class ImageProcessingError(MediaProcessingError):
    pass
