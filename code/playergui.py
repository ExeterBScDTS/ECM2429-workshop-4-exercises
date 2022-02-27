import logging
from queue import Queue
from tkinter import Tk, ttk, Button, StringVar, Label, Listbox

logger = logging.getLogger(__name__)


class PlayerGUI:
    """_summary_
    """
    def __init__(self):
        """Constructor for a simple tkinter GUI
        """
        self.__root = Tk()
        self.__root.title(__name__)

        self.start_button = Button(self.__root, text="Play", command=self.play)
        self.start_button.pack()

        self.stop_button = Button(self.__root, text="Pause", command=self.pause)
        self.stop_button.pack()

        #self.countdown_text = StringVar()
        #self.countdown_label = Label(self.__root, textvar=self.countdown_text)
        #self.countdown_label.pack()

        albums = ["a", "b"]
        albums_var = StringVar(value=albums)
        self.album_list = Listbox(self.__root, height=10, listvariable=albums_var)
        self.album_list.pack()
        self.album_list.bind("<<ListboxSelect>>", self.album_sel)
        #lbox.bind("<Double-1>", lambda e: invokeAction(lbox.curselection()))

        tracks = []
        tracks_var = StringVar(value=tracks)
        self.track_list = Listbox(self.__root, height=10, listvariable=tracks_var)
        self.track_list.pack()

        playlist = []
        playlist_var = StringVar(value=playlist)
        self.playlist = Listbox(self.__root, height=10, listvariable=playlist_var)
        self.playlist.pack()

        self._state = "ready"

    def album_sel(self, evt):
        print(evt)
        print(self.album_list.curselection())

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

