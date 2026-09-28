import sounddevice as sd
from scipy.io.wavfile import write

from stt.whisper import WhisperSTT


SAMPLE_RATE = 16000
DURATION = 5


print("Preparando STT...")
stt = WhisperSTT()

print("\nHabla durante 5 segundos...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

write("audio.wav", SAMPLE_RATE, audio)

print("Audio grabado.")
print("Transcribiendo...")

texto = stt.transcribir("audio.wav")

print("\nTranscripción:")
print(texto)