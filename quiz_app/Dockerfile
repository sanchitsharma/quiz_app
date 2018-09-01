FROM ubuntu:latest
LABEL maintainer="sanchitsharma98/quiz_app"
#MAINTAINER gcr.io/zenatix-data-archiver

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get dist-upgrade --yes && \
	apt-get install -y libpng-dev libjpeg8-dev libfreetype6-dev python3.7 python3-pip && \
	apt-get install -y libev-dev
#	apt-get install -y libpq-dev libssl-dev libcurl4-openssl-dev  libxft-dev libffi-dev libev-dev && \
#	pip install --no-cache-dir --upgrade 'pip==9' boto pyinotify #Zenalytix Section begin && \
#    apt-get install -y swig openssl libffi-dev libssl-dev check automake build-essential zlib1g zlib1g-dev autoconf libtool && \
#    apt-get install -y libdb4.8 libdb++-dev libprotobuf-c1 libprotobuf-c-dev protobuf-c-compiler  && \
#	apt-get autoremove -y && apt-get clean -y && \
#    rm -rf /var/lib/apt/lists/*
ADD requirements.txt /root/requirements.txt
RUN pip3 install --no-cache-dir -r /root/requirements.txt