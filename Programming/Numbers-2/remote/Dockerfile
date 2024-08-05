FROM python:3.10-alpine3.19

RUN apk update && apk add socat && adduser -D -h /home/chall -s /bin/bash chall
RUN pip install sympy --no-cache
COPY chall.py /home/chall/chall.py
COPY flag.txt /flag.txt
USER chall
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"python /home/chall/chall.py\""]
