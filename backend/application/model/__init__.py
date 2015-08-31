from collections import namedtuple
from enum import Enum

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'

MediaURI = namedtuple("Media", ['thumbnail', 'media'])
MediaURI.__new__.__defaults__ = (None,) * len(MediaURI._fields)

User = namedtuple("User", ['id', 'role', 'username', 'email', 'password'])
User.__new__.__defaults__ = (None,) * len(User._fields)

Media = namedtuple("Media", ['id', 'owner_id', 'media_uri', 'thumbnail_uri', 'type'])
Media.__new__.__defaults__ = (None,) * len(Media._fields)