""" A prototype music player
"""
import logging
from playergui import PlayerGUI
from musicdb import MusicDB
from wavplay import WavPlay
from threading import Thread
from queue import Queue
from time import sleep


logger = logging.getLogger(__name__)


class PlayerThread(Thread):
    """
    """
    def __init__(self, group=None, target=None, name=None,
                 args=None, *kwargs, daemon=True):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """
        """
        queueIn: Queue = self.args[0]
        queueOut: Queue = self.args[1]
        while True:
            sleep(2.5)
            queueOut.put("player")


class DatabaseThread(Thread):
    """
    """
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=True):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """
        """
        queueIn: Queue = self.args[0]
        queueOut: Queue = self.args[1]
        while True:
            sleep(0.5)
            queueOut.put("db")


if __name__ == "__main__":
    logger.info("Starting")
    feedbackQueue = Queue()
    playQueue = Queue()
    player = PlayerThread(args=(playQueue, feedbackQueue))
    player.start()
    dbQueue = Queue()
    db = DatabaseThread(args=(dbQueue, feedbackQueue))
    db.start()
    while True:
        print(feedbackQueue.get())
