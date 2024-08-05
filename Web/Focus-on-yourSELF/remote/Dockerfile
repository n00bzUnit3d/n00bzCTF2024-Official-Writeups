FROM python:3.10-alpine3.19

COPY srv/ /srv/

RUN adduser -D -h /home/chall -s /bin/bash chall && \
	pip install -r /srv/requirements.txt --no-cache && \
	chmod 755 /srv/* && \
	chmod 777 /srv/uploads/

USER chall

ENTRYPOINT ["python", "/srv/app.py"]
