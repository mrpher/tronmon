# Stage 1
FROM balenalib/raspberrypi4-64-python:3.7-latest-build as build

RUN mkdir /install
WORKDIR /install

COPY ./src/requirements.txt /requirements.txt

ENV PATH=/root/.local/bin:$PATH
RUN pip install --user -r /requirements.txt

## Stage 2
FROM balenalib/raspberrypi4-64-python:3.7-latest-run

COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

RUN install_packages jq

WORKDIR /vedirect

COPY ./src .


ENV UDEV=1

CMD ["/bin/sh","./start.sh"]