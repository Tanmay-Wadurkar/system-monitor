#Use Ubuntu as base image
FROM ubuntu:22.04

#set working directory 
WORKDIR /app

#install requiements 
RUN apt-get update &&\
    apt-get install -y\
    python3\
    procps\
    && rm -rf /var/lib/apt/list/*

#copy required files
COPY monitor.sh /app/
COPY analyze.py /app/

#make files executable 
RUN chmod +x /app/monitor.sh /app/analyze.py

#create logfile 
RUN mkdir -p /app/logs

#define env variables 
ENV TERM=xterm-256color

#Final command
CMD ["./monitor.sh"]
