import sqlite3
import logging

logger = logging.getLogger(__name__)


class MusicDB:
    """
    Interface to a SQLite3 database.
    Note that sqlite3 is thread safe, for reading, but requires
    check_same_thread=False is set in calls to connect().  By
    default check_same_thread is True, so we leave it this way
    and only access the DB from one thread.
    """
    def __init__(self, connection_uri: str) -> None:
        """
        :param connection_uri: a valid URI, e.g. "file:music.db?mode=rw"
        :type connection_uri: str
        """
        self.__connection_uri = connection_uri
        self.verify_connection()
        pass

    def verify_connection(self):
        """Ensure connection to the database is possible.
        """
        con = sqlite3.connect(self.__connection_uri, uri=True)
        con.close()
        pass
