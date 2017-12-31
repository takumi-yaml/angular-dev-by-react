 FROM python:3
 ENV PYTHONUNBUFFERED 1
 ADD . /app/
 WORKDIR /app
 RUN pip install -r requirements.txt
 RUN python3 setup.py develop
 RUN pwd
