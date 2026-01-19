from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class MediaFormat(Enum):
    MP3 = "MP3"
    FLAC = "FLAC"


@dataclass
class AudioDecoder(ABC):
    audio_data: bytes

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def decode(self) -> bytes:
        pass


@dataclass
class AudioProcessor(ABC):
    audio_data: bytes

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def process(self) -> bytes:
        pass


@dataclass
class AudioPlayer(ABC):
    volume: int
    playback_rate: float

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    def set_volume(self, volume: int) -> None:
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {volume}")
        else:
            print("Invalid volume level")


class AudioFactory(ABC):
    @abstractmethod
    def create_audio_decoder(self, audio_data: bytes) -> AudioDecoder:
        pass

    @abstractmethod
    def create_audio_processor(self, audio_data: bytes) -> AudioProcessor:
        pass

    @abstractmethod
    def create_audio_player(self, volume: int, playback_rate: float) -> AudioPlayer:
        pass

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass


class FLACAudioFactory(AudioFactory):
    def create_audio_decoder(self, audio_data: bytes) -> AudioDecoder:
        return FLACDecoder(audio_data)

    def create_audio_processor(self, audio_data: bytes) -> AudioProcessor:
        return FLACAudioProcessor(audio_data)

    def create_audio_player(self, volume: int, playback_rate: float) -> AudioPlayer:
        return FLACPlayer(volume, playback_rate)

    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC


class MP3AudioFactory(AudioFactory):
    def create_audio_decoder(self, audio_data: bytes) -> AudioDecoder:
        return MP3Decoder(audio_data)

    def create_audio_processor(self, audio_data: bytes) -> AudioProcessor:
        return MP3AudioProcessor(audio_data)

    def create_audio_player(self, volume: int, playback_rate: float) -> AudioPlayer:
        return MP3Player(volume, playback_rate)

    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3


@dataclass
class MP3Decoder(AudioDecoder):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3

    def decode(self) -> bytes:
        # Implement MP3 decoding logic
        print("Decoding MP3 audio data...")
        # Decoding process
        return self.audio_data


@dataclass
class FLACDecoder(AudioDecoder):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC

    def decode(self) -> bytes:
        # Implement FLAC decoding logic
        print("Decoding FLAC audio data...")
        # Decoding process
        return self.audio_data


@dataclass
class MP3Player(AudioPlayer):
    def play(self) -> None:
        print("Playing MP3 audio")

    def pause(self) -> None:
        print("Pausing MP3 audio")

    def stop(self) -> None:
        print("Stopping MP3 audio")

    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3


@dataclass
class FLACPlayer(AudioPlayer):
    def play(self) -> None:
        print("Playing FLAC audio")

    def pause(self) -> None:
        print("Pausing FLAC audio")

    def stop(self) -> None:
        print("Stopping FLAC audio")

    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC


@dataclass
class MP3AudioProcessor(AudioProcessor):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3

    def process(self) -> bytes:
        # Implement MP3 audio processing logic
        print("Processing MP3 audio data...")
        # Processing process
        return self.audio_data


@dataclass
class FLACAudioProcessor(AudioProcessor):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC

    def process(self) -> bytes:
        # Implement FLAC audio processing logic
        print("Processing FLAC audio data...")
        # Processing process
        return self.audio_data
