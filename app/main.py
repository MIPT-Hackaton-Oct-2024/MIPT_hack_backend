from fastapi import UploadFile, FastAPI
from fastapi.templating import Jinja2Templates
import aiohttp
import json
import pandas as pd


app = FastAPI()
templates = Jinja2Templates(directory="templates")
_test_fname = ""


@app.post("/uploadfile/")
async def upload(file_upload: UploadFile):
    data = await file_upload.read()

    global _test_fname
    _test_fname = file_upload.filename

    save_to = f"./uploads/{file_upload.filename}"

    with open(save_to, "wb") as f:
        f.write(data)

    return {"filenames": file_upload.filename}


@app.get("/test_predict/")
async def predict():
    global _test_fname

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url="http://localhost:4000/get_predictions_testmodel/",
            # json=pd.read_excel(f"./uploads/{_test_fname}").to_json(orient="records"),
            json={"key": 123},
            proxy="http://mipt-hack-ml_engine:4000/",
        ) as resp:
            data = await resp.json()
            return data


@app.get("/")
def main():
    return "Welcome!"
