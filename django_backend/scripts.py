# import uuid
# reference_id = str(uuid.uuid4())
# print(reference_id)
# 
from dotenv import load_dotenv
import httplib, urllib, base64, uuid,json
import os

load_dotenv()
headers = {
    # Request headers
    'X-Reference-Id': os.environ.get("REF_ID"),
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': os.environ.get("PRIMARY_KEY"),
}
params = urllib.urlencode({})
body = json.dumps({
  "providerCallbackHost":  os.environ.get("DOMAIN") })
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))