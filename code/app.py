""" A prototype music player
"""
import logging
from playergui import PlayerGUI
from musicdb import MusicDB
import threading
from time import sleep
import queue

logger = logging.getLogger(__name__)


class ThreadedBody:
    """_summary_
    """
    def __init__(self) -> None:
        """_summary_
        """
        self.thread = threading.Thread(target=self.worker_thread)
        self.run = True
        self.thread.start()

    def worker_thread(self):

        while self.run:
            sleep(2.5)
            print("thread")    

if __name__ == "__main__":
    logger.info("Starting")
    thread = ThreadedBody()
    for i in range(10):
        sleep(1.8)
        print(i)
    thread.run = False



