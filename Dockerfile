# Dockerfile - this is a comment. Delete me if you want.
FROM docker.io/dmilan/python-3.7-alpine-flask-restplus
#FROM python:3.7

MAINTAINER Milan Das "milan.das77@gmail.com"
ENV APP_HOME /app/docker-s3-access
#ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME
RUN pip install -r requirements-docker.txt
ENV PYTHONPATH=$PYTHONPATH:$APP_HOME

ENTRYPOINT ["python"]
CMD ["app/main.py"]
