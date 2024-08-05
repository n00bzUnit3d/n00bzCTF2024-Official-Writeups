FROM ubuntu:latest@sha256:c920ba4cfca05503764b785c16b76d43c83a6df8d1ab107e7e6610000d94315c

COPY /src/tictactoe.c /src/flag.txt /srv/
RUN apt update && apt install -y gcc socat && \
	cd /srv/ && gcc tictactoe.c -o tictactoe && \
	useradd -m -s /bin/bash chall && \
	chmod 555 tictactoe && chmod 444 flag.txt && rm tictactoe.c

USER chall

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"/srv/tictactoe\""]
