FROM ubuntu

RUN apt-get update -y

COPY ./ps_aux.py /tmp/ps_aux.py
COPY ./README.txt /tmp/README.txt

WORKDIR /tmp

RUN apt-get install -y python3
RUN apt-get install -y sqlite3

ENTRYPOINT ["/bin/bash"]
