""" A prototype music player
"""
import logging
from playergui import PlayerGUI
from musicdb import MusicDB
from wavplay import WavPlay
import threading
from threading import Thread
from queue import Empty, Queue
from time import sleep
import sys

logger = logging.getLogger(__name__)

"""
def exitfn(args):
    print("exitfn")
    print(args)
    sys.exit(1)

threading.excepthook = exitfn
"""

class PlayerThread(Thread):
    """
    """
    def __init__(self, group=None, target=None, name=None,
                 args=None, *kwargs, daemon=True):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        self.player = WavPlay()

    def run(self):
        """
        """
        queueIn: Queue = self.args[0]
        queueOut: Queue = self.args[1]
        while True:
            try:
                msg = queueIn.get_nowait()
                if msg["cmd"] == "pause":
                    self.player.paused = True
                elif msg["cmd"] == "play":
                    self.player.paused = False
                elif msg["cmd"] == "load":
                    self.player.load(msg["data"])
            except Empty:
                pass
            if self.player.paused:
                queueOut.put("paused")
                sleep(0.1)
            else:
                self.player.play()
                queueOut.put("playing")


class DatabaseThread(Thread):
    """
    """
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, daemon=True):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        # Open DB in read-only mode
        self.db = MusicDB("file:music.db?mode=ro")

    def run(self):
        """
        """
        queueIn: Queue = self.args[0]
        queueOut: Queue = self.args[1]
        while True:
            sleep(2)
            queueOut.put("db")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("Starting")
    # Create the GUI, but don't run mainloop() yet
    gui = PlayerGUI()
    feedbackQueue = Queue()
    gui.feedback = feedbackQueue
    playQueue = Queue()
    player = PlayerThread(args=(playQueue, feedbackQueue))
    player.start()
    dbQueue = Queue()
    db = DatabaseThread(args=(dbQueue, feedbackQueue))
    db.start()

    # Note that we can access methods and properties of the gui
    # because this main thread is the gui thread.  We should not
    # directly access objects in other threads.

 
    def body():
        if gui._state == "paused":
            playQueue.put({"cmd": "pause"})
        else:
            playQueue.put({"cmd": "play"})

        try:
            msg = feedbackQueue.get_nowait()
            logger.debug(f"feedback: {msg}")
        except Empty:
            pass

   
    # If no database available can insert data to play like this -
    with open("sample.wav", "rb") as f:
        playQueue.put({"cmd": "load", "data": f.read()})
    
    gui.set_after(200, body)
    gui.mainloop()
