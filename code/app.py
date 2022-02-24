""" A prototype music player
"""
import logging
from playergui import PlayerGUI
from musicdb import MusicDB
from wavplay import WavPlay
from threading import Thread
from queue import Empty, Queue
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
        self.player = WavPlay()

    def run(self):
        """
        """
        queueIn: Queue = self.args[0]
        queueOut: Queue = self.args[1]
        with open("sample.wav", "rb") as f:
            self.player.load(f.read())
        while True:
            self.player.play()
            #sleep(0.5)
            queueOut.put("playing")


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
        try:
            msg = feedbackQueue.get_nowait()
            print(msg)
            print(gui.state())
            if gui.state == "paused":
                print("Doing pause")
                playQueue.put("pause")
        except Empty:
            pass

    gui.set_after(20, body)
    gui.mainloop()

