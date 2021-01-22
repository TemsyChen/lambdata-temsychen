FROM ubuntu

ENV PYTHONBUFFER=1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy && \
    pip3 install --index-url https://test.pypi.org/simple/ --no-deps lambdata-temsychen