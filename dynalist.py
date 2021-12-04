# https://apidocs.dynalist.io/#general
# export DYNALIST_TOKEN=your-token-here

import requests, json, os

token= os.environ.get('DYNALIST_TOKEN')

response=requests.post("https://dynalist.io/api/v1/file/list", json = {"token": token})
resposne_json = json.loads(response.text)
print(resposne_json)

