FROM python:3.8.13-slim-buster

WORKDIR /app

COPY requirement.txt requirement.txt

RUN pip3 install -r requirement.txt

COPY . .

CMD [ "python3" , "manage.py", "runserver", "0.0.0.0:8000"]
