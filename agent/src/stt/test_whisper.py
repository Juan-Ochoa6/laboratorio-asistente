from whisper import WhisperSTT


print("Iniciando prueba de STT...")

stt = WhisperSTT()

texto = stt.transcribir("audio.wav")

print("\nTranscripción:")
print(texto)