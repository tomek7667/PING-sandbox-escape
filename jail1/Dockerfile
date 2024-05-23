FROM ubuntu
FROM python:3.9

COPY ./main.py /home/ctf
COPY ./flag.txt /home/ctf

RUN apt update
RUN apt install -y \
    socat
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf
USER ctf

EXPOSE 3000
ENTRYPOINT socat tcp-l:3000,fork,reuseaddr exec:'python3 main.py' && /bin/bash
