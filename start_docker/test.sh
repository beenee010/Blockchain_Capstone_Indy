#!/bin/bash

indy-cli make_pool.txt

cd /home/indy/

tar xvzf /home/indy/python3-indy-1.16.0.tar.gz
# CMD ["python3","setup.py","install"]
cd /home/indy/python3-indy-1.16.0

python3 setup.py install
