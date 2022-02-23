import logging
from sys import float_repr_style
import pyaudio
import wave
import io

logger = logging.getLogger(__name__)


class WavPlay:
    CHUNK = 1024

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.paused = False
  
    def __del__(self):
        # close PyAudio
        logger.warning("close")
        self.p.terminate()
        
    def play(self, audio_in: bytes):
        """Play WAV audio data

        :param audio_in: audio_in is bytes containing WAV audio.
        :type audio_in: bytes
        """

        wf = wave.open(io.BytesIO(audio_in), 'rb') 

        stream = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)
     
        self._playframes(wf, stream)
        # stop stream
        stream.stop_stream()
        stream.close()

    def _playframes(self, wf, stream):
        # read data
        data = wf.readframes(WavPlay.CHUNK)
        # play stream
        while len(data) > 0:
            if not self.paused:
                stream.write(data)
                data = wf.readframes(WavPlay.CHUNK)


if __name__ == "__main__":
    wp = WavPlay()
    with open("sample.wav", "rb") as f:
        wp.play(f.read())
    with open("sample.wav", "rb") as f:
        wp.play(f.read())