from pathlib import Path


class AudioFile:
    ext: str
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError(f"Invalid file format {filepath.suffix} instead of {self.ext}")
        self.filepath = filepath


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")

class WavFile(AudioFile):
    ext = ".wav"

    def paly(self) -> None:
        print(f"playing {self.filepath} as wav")

class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")


if __name__ == "__main__":
    mp3 = MP3File(Path('mp3/route.mp3'))
    mp3.play()
    wav = WavFile(Path('wav/route.wav'))
    wav.paly()
    ogg = OggFile(Path('ogg/route.ogg'))
    ogg.play()
    not_mp3 = MP3File(Path('mp3/route.mp5'))
    not_mp3.play()
