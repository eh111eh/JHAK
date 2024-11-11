import sounddevice as sd
import numpy as np

def test_audio_input():
    fs = 16000  # Sample rate
    duration = 5  # seconds
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    print(audio_data)

if __name__ == "__main__":
    test_audio_input()
