FROM ubuntu:16.04

ARG uid=1000

# Install environment
RUN apt-get update
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y vim
RUN apt-get update -y && apt-get install -y \
        git \
        wget \
        python3.6 \
        python3-pip \
        python-setuptools \
        python3-nacl \
        apt-transport-https \
        ca-certificates
RUN pip3 install -U \
        'pip<10.0.0' \
        setuptools
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE7709D068DB5E88
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BD33704C

RUN useradd -ms /bin/bash -l -u $uid indy
RUN apt-get update -y

RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common

RUN add-apt-repository "deb https://repo.sovrin.org/sdk/deb xenial stable"
RUN apt-get update -y
RUN apt-get install -y libnullpay
RUN apt-get install -y libvcx
RUN apt-get install -y indy-cli
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN pip install --upgrade python3-indy

ADD genesis /home/indy/genesis
ADD make_pool.txt /home/indy/make_pool.txt
ADD test.sh /home/indy/start.sh
ADD init.sh /home/indy/init.sh

ADD utils.py /home/indy/utils.py

ADD generate_did.py /home/indy/generate_did.py
ADD get_did.py /home/indy/get_did.py

ADD generate_attrib.py /home/indy/generate_attrib.py
ADD get_attrib.py /home/indy/get_attrib.py

# WORKDIR /home/indy/python3-indy-1.16.0
# CMD ["python3","setup.py","install"]

WORKDIR /home/indy

RUN chmod -R 777 /home/indy/init.sh
# ENTRYPOINT ["./init.sh"]
USER indy
