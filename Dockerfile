FROM python:3.9.0
LABEL maintainer="viridis959@gmail.com"
ENV PYTHONUNBUFFERED 1

RUN mkdir /docker
COPY . /docker
WORKDIR /docker/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uwsgi", "-i", "uwsgi.ini"]
