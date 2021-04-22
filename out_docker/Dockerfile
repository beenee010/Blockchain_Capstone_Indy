FROM indybase

ARG uid=1000

# Install environment
RUN apt-get update
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common
# RUN add-apt-repository ppa:jonathonf/python-3.6
RUN add-apt-repository ppa:deadsnakes/ppa
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
# RUN echo "deb https://repo.sovrin.org/deb xenial master" >> /etc/apt/sources.list
# RUN echo "deb https://repo.sovrin.org/sdk/deb xenial master" >> /etc/apt/sources.list

RUN useradd -ms /bin/bash -l -u $uid indy
RUN apt-get update -y
# RUN apt-get install -y indy-node
# RUN apt-get install libindy
# RUN pip3 install python3-indy

RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common

RUN add-apt-repository "deb https://repo.sovrin.org/sdk/deb xenial stable"
RUN apt-get update -y
RUN apt-get install -y libnullpay
RUN apt-get install -y libvcx
RUN apt-get install -y indy-cli
# RUN pip install --upgrade pip
# RUN pip install --upgrade pip
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN pip install --upgrade python3-indy

ADD genesis /home/indy/genesis
ADD make_pool.txt /home/indy/make_pool.txt
ADD test.sh /home/indy/start.sh
ADD generate_did.py /home/indy/generate_did.py
ADD utils.py /home/indy/utils.py
# RUN wget -P /home/indy/ https://files.pythonhosted.org/packages/0a/e7/8fad37b523d0d14cc55d22cc8ffb7a381c9384d142f006000fe3295b73bf/python3-indy-1.16.0.tar.gz
# RUN tar xvzf /home/indy/python3-indy-1.16.0.tar.gz
ADD python3-indy-1.16.0 /home/indy/python3-indy-1.16.0
# RUN cd python3-indy-1.16.0
WORKDIR /home/indy/python3-indy-1.16.0
CMD ["python3","setup.py","install"]
# ADD python3-indy-1.16.0.tar /home/indy/python3-indy-1.16.0.tar 
# CMD indy-cli "make_pool.txt"

# USER indy
WORKDIR /home/indy

RUN chmod -R 777 /home/indy/start.sh
ENTRYPOINT ["./start.sh"]
# CMD ["tar","xvf","python3-indy-1.16.0.tar"]
USER indy
