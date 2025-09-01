from fastapi import APIRouter, Depends
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from src.controllers.audio_controller import AudioController

templates = Jinja2Templates(directory='templates')

router = APIRouter()

audio_controller = AudioController()

@router.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@router.post('/encrypt-audio')
async def exec_encrypt_audio(request: Request, text: str = Form(...)):
    audio_path, audio_name = audio_controller.encrypt_audio(text)
    return FileResponse(audio_path, media_type='audio/mpeg', filename=audio_name)

@router.post('/decrypt-audio')
async def exec_decrypt_audio(request: Request, file: UploadFile = File(...)):
    file_content = await file.read()
    text = audio_controller.decrypt_audio(file_content)
    if text:
        return templates.TemplateResponse('result.html', {'request': request, 'action': 'success', 'text': text})
    else:
        return templates.TemplateResponse('result.html', {'request': request, 'action': 'error', 'message': 'Não foi possível decodificar o áudio.'})