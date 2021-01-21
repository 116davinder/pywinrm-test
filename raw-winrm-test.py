#! /usr/local/python3

from requests_ntlm import HttpNtlmAuth
import requests

print("Starting NTLM Script")
host = input("hostname of windows with port: ")
user = input("username of windows: ")
password = input("password of windows: ")
message = "whoami"

s = requests.session()

s.auth = HttpNtlmAuth(
    username=user,
    password=password,
    send_cbt=False
)

_p = s.prepare_request(requests.Request('POST', "http://" + host + "/wsman", data=message))

response = s.send(_p)

if response.status_code == 401:
    print("the specified credentials were rejected by the server")

print(response.status_code, response.content, response)
