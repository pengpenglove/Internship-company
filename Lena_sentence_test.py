# _*_coding:utf-8_*_
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd

def sendjsondata(sentence):

    datajson = """{"chnl":"pc","chnlUsrId":"b3ec1114-b6ef-4bf1-acf3-cd51f7dbd766","lan":"en",
                  "query":{
                      "type":"text",
                      "msg":"%s",
                      "id":"afdfa23faasdf231"
                  },
                  "context":null,
                  "timestamp":"12432467342"
              }""" % sentence

    headers = {'Content-Type': 'application/json'}
    url = 'http://10.110.147.195:21000'
    response = requests.post(url, data=datajson)
    responsejson = response.json()
    # print(responsejson['semanticFrames'][0])
    # print(responsejson['semanticFrames'][1])
    # print(datajson)

    try:
        responsejson['semanticFrames'][0]['domain']['name']
        responsejson['semanticFrames'][0]['domain']['confidence']
    except BaseException:
        domainname0 = '000'
        domainconfidence0 = '000'
    else:
        domainname0 = responsejson['semanticFrames'][0]['domain']['name']
        domainconfidence0 = responsejson['semanticFrames'][0]['domain']['confidence']
    try:
        responsejson['semanticFrames'][0]["intent"]["code"]
        responsejson['semanticFrames'][0]['intent']['confidence']
    except BaseException:
        intentname0 = '000'
        intentconfidence0 = '000'
    else:
        intentname0 = responsejson['semanticFrames'][0]["intent"]["code"]
        intentconfidence0 = responsejson['semanticFrames'][0]['intent']['confidence']
    try:
        responsejson['semanticFrames'][0]['subintent']['code']
        responsejson['semanticFrames'][0]['subintent']['confidence']
    except BaseException:
        subintentname0 = '000'
        subintentconfidence0 = '000'
    else:
        subintentname0 = responsejson['semanticFrames'][0]['subintent']['code']
        subintentconfidence0 = responsejson['semanticFrames'][0]['subintent']['confidence']

    try:
        responsejson['semanticFrames'][1]['domain']['name']
        responsejson['semanticFrames'][1]['domain']['confidence']
    except BaseException:
        domainname1 = '000'
        domainconfidence1 = '000'
    else:
        domainname1 = responsejson['semanticFrames'][1]['domain']['name']
        domainconfidence1 = responsejson['semanticFrames'][1]['domain']['confidence']
    try:
        responsejson['semanticFrames'][1]["intent"]["code"]
        responsejson['semanticFrames'][1]['intent']['confidence']
    except BaseException:
        intentname1 = '000'
        intentconfidence1 = '000'
    else:
        intentname1 = responsejson['semanticFrames'][1]["intent"]["code"]
        intentconfidence1 = responsejson['semanticFrames'][1]['intent']['confidence']
    try:
        responsejson['semanticFrames'][1]['subintent']['code']
        responsejson['semanticFrames'][1]['subintent']['confidence']
    except BaseException:
        subintentname1 = '000'
        subintentconfidence1 = '000'
    else:
        subintentname1 = responsejson['semanticFrames'][1]['subintent']['code']
        subintentconfidence1 = responsejson['semanticFrames'][1]['subintent']['confidence']

    try:
        responsejson['semanticFrames'][2]['domain']['name']
        responsejson['semanticFrames'][2]['domain']['confidence']
    except BaseException:
        domainname2 = '000'
        domainconfidence2 = '000'
    else:
        domainname2 = responsejson['semanticFrames'][2]['domain']['name']
        domainconfidence2 = responsejson['semanticFrames'][2]['domain']['confidence']
    try:
        responsejson['semanticFrames'][2]["intent"]["code"]
        responsejson['semanticFrames'][2]['intent']['confidence']
    except BaseException:
        intentname2 = '000'
        intentconfidence2 = '000'
    else:
        intentname2 = responsejson['semanticFrames'][2]["intent"]["code"]
        intentconfidence2 = responsejson['semanticFrames'][2]['intent']['confidence']
    try:
        responsejson['semanticFrames'][2]['subintent']['code']
        responsejson['semanticFrames'][2]['subintent']['confidence']
    except BaseException:
        subintentname2 = '000'
        subintentconfidence2 = '000'
    else:
        subintentname2 = responsejson['semanticFrames'][2]['subintent']['code']
        subintentconfidence2 = responsejson['semanticFrames'][2]['subintent']['confidence']

    if (domainname1 !='000') :
        if ((domainname2 !='000')) :
            return [[domainname0, domainconfidence0, intentname0, intentconfidence0, subintentname0, subintentconfidence0],
                    [domainname1, domainconfidence1, intentname1, intentconfidence1, subintentname1, subintentconfidence1],
                    [domainname2, domainconfidence2, intentname2, intentconfidence2, subintentname2, subintentconfidence2]]
        else:
            return [[domainname0, domainconfidence0, intentname0, intentconfidence0, subintentname0, subintentconfidence0],
                    [domainname1, domainconfidence1, intentname1, intentconfidence1, subintentname1, subintentconfidence1]]
    else :
        return [[domainname0, domainconfidence0, intentname0, intentconfidence0, subintentname0, subintentconfidence0]]


if __name__ == '__main__':
    sentencetest = 'wifi error, shutting down takes long time and blue screen error pops out'
    requestslist = sendjsondata(sentencetest)
    print(len(requestslist))