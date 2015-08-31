from collections import namedtuple

MediaURI = namedtuple("Media", ['thumbnail', 'media'])
MediaURI.__new__.__defaults__ = (None,) * len(MediaURI._fields)
