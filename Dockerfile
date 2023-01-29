FROM python:3.8-slim-buster

RUN /bin/cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo 'Europe/Moscow' > /etc/timezone && \
    apt update 

RUN apt -y install cron

WORKDIR /
