FROM python:3
ENV PYTHONUNBUFFERED 1
#bad solution :(
ENV SLACK_BOT_TOKEN "xoxb-632564569603-632578101859-pmoqj0DnSfMs1tLjDTVTt3eR"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/