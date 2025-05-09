from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, Request, File, HTTPException

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates


app = FastAPI()
UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(exist_ok=True)

app.mount(
    '/uploader/static', 
    StaticFiles(directory='uploader/static'), 
    name='static'
)

templates = Jinja2Templates(directory='uploader/static/templates')


@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/uploader')
def upload_file(file: UploadFile = File(...)):
    try:
        file_path = UPLOAD_DIR / file.filename
        with file_path.open('wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    
    except shutil.Error as ex:
        raise HTTPException(status_code=500, detail=f'Error: {str(ex)}')
    
    except (AttributeError, ValueError) as ex:
        raise HTTPException(status_code=400, detail=f'Error: {str(ex)}')

    else:
        return {'filename': file.filename, 'message': 'Upload com sucesso'}
    
