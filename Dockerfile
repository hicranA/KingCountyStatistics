FROM python:3.10.4-slim-bullseye

WORKDIR /app

COPY requirement.txt requirement.txt

RUN pip3 install -r requirement.txt

COPY . .

CMD [ "python3" , "manage.py", "runserver", "0.0.0.0:8000"]
