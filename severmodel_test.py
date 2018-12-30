import simplejson as json
import requests
import xlrd
import xlwt
import re


sentence="How to apply new production account"
datajson ="""{"chnl":"pc","chnlUsrId":"b3ec1114-b6ef-4bf1-acf3-cd51f7dbd766","lan":"en",
    "query":{
        "type":"text",
        "msg":"小咖遇大咖",
        "id":"afdfa23faasdf231"
    },
    "context":null,
    "timestamp":"12432467342"
}"""

# print(json.dumps(datajson))
headers = {'Content-Type': 'application/json'}
url='http://192.168.3.9:21000'
response = requests.post(url, data=datajson)
responsejson=response.json()
print(responsejson)

print(responsejson['semanticFrames'][0]['domain']['name'])
print(responsejson['semanticFrames'][0]['domain']['confidence'])
print(responsejson['semanticFrames'][0]['intent']['code'])
print(responsejson['semanticFrames'][0]['intent']['confidence'])
subintentname = responsejson['semanticFrames'][0]['subintent']['code']
subintentconfidence = responsejson['semanticFrames'][0]['subintent']['confidence']
print(subintentname)
print(subintentconfidence)