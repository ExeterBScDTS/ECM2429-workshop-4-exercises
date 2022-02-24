import logging
from queue import Queue
from tkinter import Tk, ttk, Button, StringVar, Label

logger = logging.getLogger(__name__)


class PlayerGUI:
    """_summary_
    """
    def __init__(self):
        """Constructor for a simple tkinter GUI
        """
        self.__root = Tk()
        self.__root.title("Countdown")

        self.start_button = Button(self.__root, text="Play", command=self.play)
        self.start_button.pack()

        self.stop_button = Button(self.__root, text="Pause", command=self.pause)
        self.stop_button.pack()

        self.countdown_text = StringVar()
        self.countdown_label = Label(self.__root, textvar=self.countdown_text)
        self.countdown_label.pack()

        self._state = "ready"

    def countdown(self):
        # after() does not block, so do this first.
        # Called after a number of milliseconds.
        # Choose a rate that makes sense for your application.
        self.__root.after(500, self.countdown)
        if self.deadline:
            remaining = self.deadline - datetime.now()
            self.countdown_text.set(remaining)

    def play(self):
        """The play action.
        """
        logger.debug("play")
        self._state = "play"

    def pause(self):
        """The pause action.
        """
        logger.debug("pause")
        self._state = "paused"

    def _after(self):
        self.__root.after(self._ms, self._after)
        self._func()

    def set_after(self, ms, func):
        self.__root.after(ms, self._after)
        self._ms = ms
        self._func = func

    def state(self):
        return(self._state)

    def mainloop(self):
        self.__root.mainloop()


if __name__ == "__main__":
    gui = PlayerGUI()
    gui.mainloop()

