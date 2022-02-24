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
            try:
                msg = queueIn.get_nowait()
                if msg == "pause":
                    self.player.paused = True
                elif msg == "play":
                    self.player.paused = False
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
            print("Doing pause")
            playQueue.put("pause")
        else:
            playQueue.put("play")

        try:
            msg = feedbackQueue.get_nowait()
            logger.debug(f"feedback: {msg}")
        except Empty:
            pass

    gui.set_after(200, body)
    gui.mainloop()

