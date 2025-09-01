from src.services.audio_service import AudioService
from src.services.image_service import ImageService

class AudioController:

    def __init__(self):
        self._audio_service = AudioService()
        self._image_service = ImageService()
        self._image_size = (833, 622)

    def encrypt_audio(self, text: str) -> str:
        image = self._image_service.generate_image_with_text(text=text, size=self._image_size)
        audio_path, audio_name, _ = self._audio_service.image_to_audio(img=image)
    
        return audio_path, audio_name
    
    def decrypt_audio(self, audio_file: bytes) -> str:
        image = self._audio_service.audio_to_image(audio_bytes=audio_file, size=self._image_size)
        text = self._image_service.image_to_text(image)

        return text