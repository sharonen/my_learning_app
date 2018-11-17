FROM python:3.7

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean


RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
