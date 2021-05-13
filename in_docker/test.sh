#!/bin/bash

set -e

email=${1}

# indy-cli make_pool.txt

# cd /home/indy/

# tar xvzf /home/indy/python3-indy-1.16.0.tar.gz
# CMD ["python3","setup.py","install"]
# cd /home/indy/python3-indy-1.16.0

python3 generate_did.py "${email}"

# python3 setup.py install
