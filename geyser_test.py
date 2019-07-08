#!/usr/bin/env python
""" Script for pulling data from GeyserTimes.
        Future plans to turn into a function library.
"""

import requests

# Working pull request:
# https://www.geysertimes.org/api/v5/entries/1514790000/1562623085/old+faithful

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

print r.status_code