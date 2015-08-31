import pymongo
from greplin import scales

from application.model import Media


class MediasBackend(object):
    """
    Controls media model and media data fetching from database
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
        self._medias = self._db[config.mongo.media_collection]

    def fetch_medias(self, user_id, start=0, max_size=20):
        """
        Fetch all medias of user matching user_id
        :param user_id:
        :type user_id: int
        :param start: the document index from which we should fetch
        :type start: int
        :param max_size: the number of documents to fetch at a time
        :return: list of medias, else None
        :rtype: dict[str, T] | None
        """
        raise NotImplementedError()
