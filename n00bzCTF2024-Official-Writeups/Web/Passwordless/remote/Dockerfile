FROM python:3.10-alpine3.19

COPY srv/ /srv/
COPY flag.txt /flag.txt

RUN adduser -D -h /home/chall -s /bin/bash chall && \
	pip install -r /srv/requirements.txt --no-cache && \
	chmod 755 /srv/*

USER chall

ENTRYPOINT ["python", "/srv/app.py"]
