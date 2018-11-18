FROM python:3.7

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

 
RUN mkdir -p /efs/code
WORKDIR /efs/code
ADD requirements.txt /efs/code
RUN pip install -r requirements.txt
ADD . /efs/code

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
