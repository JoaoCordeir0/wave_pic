# 🎵 Wave Pic

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101.0-green)
![Tailwind](https://img.shields.io/badge/TailwindCSS-3.3-purple)

**Wave Pic** é um projeto que permite **codificar mensagens em áudios** e também **decodificar o áudio para obter o texto criptografado**, usando Python, FastAPI e TailwindCSS.  
Ele funciona como um pequeno serviço web com upload de arquivos e conversão automática.

---

## Funcionalidades

- Codificar mensagens em áudio e obter o áudio.  
- Decodificar áudio e obter o texto.  

---

## Comandos para rodar
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate # Para Linux
venv/Script/Activate # Para Windows
```
```bash
pip install -r requirements.txt
```
```bash
uvicorn main:app --reload
```

## Swagger
http://127.0.0.1:8000/docs