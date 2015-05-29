import requests
import json

"""
Nota bene: This module requires the python module "requests" to be installed. This is simply done by typing
"pip install requests"
in a terminal, as long as the python package manager pip is installed.
"""

def sendRecipientsAsPost(recipients, serverUrl):
    payload = []
    for r in recipients:
        if not r:
            continue
        d = {"Email": r, "Box_Id": "Box_1"}
        payload.append(d)

    """ Tests sending a HTTP Post request with payload. """
    print("Sending POST to:", serverUrl)
    payload = json.dumps(payload)
    print("Payload:", payload)
    r = requests.post(serverUrl, data=payload)
    print("Response:", r.text)
