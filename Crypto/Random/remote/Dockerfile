FROM ubuntu:latest@sha256:c920ba4cfca05503764b785c16b76d43c83a6df8d1ab107e7e6610000d94315c

COPY server.cpp /srv
RUN apt update && apt install -y g++ socat && \
	cd /srv/ && g++ server.cpp -o random && useradd -m -s /bin/bash chall && \
	chmod 555 random && find . -maxdepth 1 -type f ! -name 'random' -exec rm -f {} \;

USER chall

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"/srv/random\""]
