import os
import dotenv

dotenv.load_dotenv(override=True)

os.makedirs('tmp', exist_ok=True)

class Config:

    ENV = os.getenv('ENV', 'development')
    PROJECT_INFO = {
        'info': {
            'name': 'WavePic',
        },
        'dev': 'João Victor Cordeiro',
        'date': '2025-09-01',
    }