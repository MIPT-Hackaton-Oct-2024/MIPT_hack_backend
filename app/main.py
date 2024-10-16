from fastapi import UploadFile, FastAPI
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/uploadfile/")
async def upload(file_upload: UploadFile):
    data = await file_upload.read()

    save_to = f"./uploads/{file_upload.filename}"

    with open(save_to, "wb") as f:
        f.write(data)

    return {"filenames": file_upload.filename}


@app.get("/")
def main():
    return "Welcome!"
