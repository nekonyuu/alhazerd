import passlib
import pymongo
from greplin import scales

from application.model import User, UserRole
from application.common.exceptions import DuplicateUser


class UsersBackend(object):
    """
    Controls user model and user data fetching from database
    """

    requests = scales.IntStat('requests')
    latency = scales.PmfStat('latency')

    def __init__(self, config):
        """
        :param config:
        :type config: application.common.tools.Map
        :return:
        """
        scales.init(self, '/backend/users')
        self._connection = None
        self._db_name = config.mongo.db_name

        replica_set = config.mongo.replicaset_name if 'replicaset_name' in config.mongo else None
        self._connection = pymongo.MongoClient(
            config.mongo.uri,
            replicaSet=replica_set,
            maxPoolSize=config.mongo.max_pool_size,
            waitQueueMultiple=config.mongo.wait_queue_multiple,
            waitQueueTimeoutMS=config.mongo.wait_queue_timeout_ms,
            tz_aware=True
        )
        self._db = self._connection[self._db_name]
        self._users = self._db[config.mongo.user_collection]

    def register(self, username, email, password):
        """
        Register the new user
        :param username:
        :type username: str
        :param email:
        :type email: str
        :param password:
        :type password: str
        :return:
        :rtype: None
        :raise DuplicateUser: the username or email already exists
        """
        raise NotImplementedError()

    def authenticate(self, username, password):
        """
        Validate login/password of a user
        :param username:
        :type username: str
        :param password:
        :type password: str
        :return: the user id if authenticated, else None
        :rtype: bool | None
        """
        raise NotImplementedError()

    def fetch_user(self, user_id):
        """
        Fetch user_id informations
        :param user_id:
        :type user_id: int
        :return: informations about the user if exists, else None
        :rtype: dict[str, T] | None
        """
        raise NotImplementedError()
