FROM python:3.10-alpine3.19

RUN apk update && apk add socat && adduser -D -h /home/chall -s /bin/bash chall
COPY server.py /home/chall/server.py
COPY flag.txt /flag.txt
USER chall
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"python /home/chall/server.py\""]
