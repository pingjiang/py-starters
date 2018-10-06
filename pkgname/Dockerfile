FROM python:3.6-stretch

ARG PKG=http://localhost:9999/pkgname.tar.gz

# debian mirrors
RUN apt-get update && apt-get install -y \
  curl

WORKDIR /workspace

# download source code
RUN mkdir -p /tmp/pkgname_src && \
    cd /tmp/pkgname_src && \
    curl -SL ${PKG} | tar xzvf - && \
    cd pkgname && \
    pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt && \
    python3 setup.py install && \
    pkgname_cli --help && \
    rm -rf /tmp/pkgname_src

VOLUME [ "/workspace" ]

ENTRYPOINT /bin/bash
