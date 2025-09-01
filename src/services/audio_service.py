import numpy as np
import wave
import io
from datetime import datetime

class AudioService:

    def __init__(self):
        pass

    def image_to_audio(self, img: np.ndarray) -> tuple:
        data = np.array(img).flatten()
        data = (data / 255.0 * 32767).astype(np.int16)

        sample_rate = 44100 
        duration = len(data) / sample_rate

        current_date = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'audio_{current_date}.wav'

        with wave.open(f'tmp/{filename}', 'w') as wav_file:
            wav_file.setnchannels(1)  
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(data.tobytes())

        return f'tmp/{filename}', filename, duration
    
    def audio_to_image(self, audio_bytes: bytes, size: tuple) -> np.ndarray:
        with wave.open(io.BytesIO(audio_bytes), 'rb') as wav_file:
            n_frames = wav_file.getnframes()
            audio_data = wav_file.readframes(n_frames)

        data = np.frombuffer(audio_data, dtype=np.int16)

        pixels = ((data.astype(np.float32) / 32767.0) * 255).astype(np.uint8)

        pixels = pixels[: size[0] * size[1]]

        img_array = pixels.reshape(size[1], size[0])

        return img_array