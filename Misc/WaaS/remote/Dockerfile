FROM python:3.9-alpine3.19

COPY chall.py flag.txt fake_flag.txt /
RUN apk update && apk add socat && chmod 444 /chall.py /flag.txt /fake_flag.txt

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"python /chall.py\""]
