# user management
class DuplicateUser(Exception):
    pass

# media processing
class MediaProcessingError(Exception):
    pass

class VideoProcessingError(MediaProcessingError):
    pass

class ImageProcessingError(MediaProcessingError):
    pass