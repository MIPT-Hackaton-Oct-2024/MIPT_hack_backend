FROM python:3.9-slim

WORKDIR /code

RUN mkdir uploads

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000" ]