from faster_whisper import WhisperModel

print("Cargando modelo...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcribiendo audio...")

segments, info = model.transcribe(
    "audio.wav",
    language="es"
)

print("Idioma detectado:", info.language)
print("\nTranscripción:")

for segment in segments:
    print(segment.text)
