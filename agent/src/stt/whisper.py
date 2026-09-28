from faster_whisper import WhisperModel


class WhisperSTT:

    def __init__(self):
        print("Cargando modelo Whisper...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def transcribir(self, archivo_audio):
        segments, info = self.model.transcribe(
            archivo_audio,
            language="es"
        )

        texto = ""

        for segment in segments:
            texto += segment.text

        return texto.strip()