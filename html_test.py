import requests
import json

"""
Nota bene: This module requires the python module "requests" to be installed. This is simply done by typing
"pip install requests"
in a terminal, as long as the python package manager pip is installed.
"""

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}


def testPost():
    """ Tests sending a HTTP Post request with payload. """
    r = requests.post(url, data=json.dumps(payload))
    print(r)
