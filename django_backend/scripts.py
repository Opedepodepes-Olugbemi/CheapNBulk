# import uuid
# reference_id = str(uuid.uuid4())
# print(reference_id)
# 
# from dotenv import load_dotenv
import http.client as httplib
import urllib, base64, uuid,json
import os

# load_dotenv()
headers = {
    # Request headers
    'X-Reference-Id': "db7269f4-e7de-435c-83ec-3026660b02e6",
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "e619a30053ea4f4e93c2938977af8585",
}
params = urllib.parse.urlencode({})
body = json.dumps({
  "providerCallbackHost": "51.20.212.22" })
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
    print(e)

# <VirtualHost *:80>
#   ServerName 51.20.212.22
#   DocumentRoot /home/ubuntu/CheapNBulk/django_backend
  
#   Alias /static/ /home/ubuntu/CheapNBulk/django_backend/static
  
#   <Directory /home/ubuntu/CheapNBulk/django_backend/static>
#     Require all granted
#   </Directory>
  
#   WSGIDaemonProcess django_backend python-home=/home/ubuntu/.venv python-path=/home/ubuntu/CheapNBulk/django_backend
#    WSGIProcessGroup django_backend
#   WSGIScriptAlias / /home/ubuntu/CheapNBulk/django_backend/django_backend/wsgi.py
  
#   <Directory /home/ubuntu/CheapNBulk/django_backend/django_backend>
#     <Files wsgi.py>
#       Require all granted
#     </Files>
#   </Directory>
# </VirtualHost>

# <VirtualHost *:80>
#         # The ServerName directive sets the request scheme, hostname and port that
#         # the server uses to identify itself. This is used when creating
#         # redirection URLs. In the context of virtual hosts, the ServerName
#         # specifies what hostname must appear in the request's Host: header to
#         # match this virtual host. For the default virtual host (this file) this
#         # value is not decisive as it is used as a last resort host regardless.
#         # However, you must set it for any further virtual host explicitly.
#         #ServerName www.example.com

#         ServerAdmin webmaster@localhost
#         DocumentRoot /var/www/html

#         # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
#         # error, crit, alert, emerg.
#         # It is also possible to configure the loglevel for particular
#         # modules, e.g.
#         #LogLevel info ssl:warn

#         ErrorLog ${APACHE_LOG_DIR}/error.log
#         CustomLog ${APACHE_LOG_DIR}/access.log combined

#         # For most configuration files from conf-available/, which are
#         # enabled or disabled at a global level, it is possible to
#         # include a line for only one particular virtual host. For example the
#         # following line enables the CGI configuration for this host only
#         # after it has been globally disabled with "a2disconf".
#         #Include conf-available/serve-cgi-bin.conf
# </VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet