import logging

logger = logging.getLogger(__name__)

class WavPlay:
    def __init__(self) -> None:
        pass
    
    def play(self, data: bytes):
        pass

if __name__ == "__main__":
    wp = WavPlay()
    with open("sample.wav", "rb") as f:
        wp.play(f.read())

