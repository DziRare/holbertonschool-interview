#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{ip1:d}.{ip2:d}.{ip3:d}.{ip4:d} - [{date}] \"GET /projects/260 HTTP/1.1\" {error_code} {file_size}\n".format(
        ip1=random.randint(1, 255), ip2=random.randint(1, 255), ip3=random.randint(1, 255), ip4=random.randint(1, 255),
        date=datetime.datetime.now(),
        error_code=random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        file_size=random.randint(1, 1024)
    ))
    sys.stdout.flush()