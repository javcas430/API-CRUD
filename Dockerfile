# Dockerfile, Image, Container

FROM python:3.8.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

CMD ["uvicorn", "main:app","--reload", "--env-file",".env", "--host", "0.0.0.0", "--port", "80"]