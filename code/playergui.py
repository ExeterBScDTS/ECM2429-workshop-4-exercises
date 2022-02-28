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

        self.albums_var = StringVar(value=[])
        self.album_list = Listbox(self.__root, height=10, listvariable=self.albums_var)
        self.album_list.pack()
        self.album_list.bind("<<ListboxSelect>>", self.album_sel)
        #lbox.bind("<Double-1>", lambda e: invokeAction(lbox.curselection()))

        self.tracks_var = StringVar(value=[])
        self.track_list = Listbox(self.__root, height=10, listvariable=self.tracks_var)
        self.track_list.pack()
        self.track_list.bind("<<ListboxSelect>>", self.track_sel)

        self.playlist = []
        self.playlist_var = StringVar(value=self.playlist)
        self.playlist_list = Listbox(self.__root, height=10, listvariable=self.playlist_var)
        self.playlist_list.pack()
        self.playlist_list.bind("<<ListboxSelect>>", self.playlist_sel)

        self.db_cmd = None
        self.db_data = None
        self._state = "ready"

    def set_albums(self, albums):
        self.albums = albums
        self.albums_var.set(albums)

    def album_sel(self, evt):
        print(evt)
        sel = self.album_list.curselection()[0]
        logger.debug(f"selected {self.albums[sel]}")
        self.db_cmd = "tracks"
        self.db_data = self.albums[sel]

    def set_tracks(self, tracks):
        self.tracks = tracks
        self.tracks_var.set(tracks)

    def track_sel(self, evt):
        print(evt)
        sel = self.track_list.curselection()[0]
        logger.debug(f"selected {self.tracks[sel]}")
        self.playlist.append(self.tracks[sel])
        self.playlist_var.set(self.playlist)


    def playlist_sel(self, evt):
        print(evt)
        sel = self.playlist.curselection()[0]
        logger.debug(f"selected {self.tracks[sel]}")


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

