# _*_coding:utf-8_*_
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd


def open_files(filepath):
    # 打开excel文件并修改该文件
    new_content = xlrd.open_workbook(filepath,encoding_override="utf-8")
    new_sheet = new_content.sheets()[0]
    return new_sheet

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
    #195 lena
    url = 'http://10.110.147.195:21000'
    response = requests.post(url, data=datajson)
    responsejson = response.json()
    # print(responsejson)
    # print(datajson)

    try:
        responsejson['semanticFrames'][0]['domain']['name']
        responsejson['semanticFrames'][0]['domain']['confidence']
    except BaseException:
        domainname = '000'
        domainconfidence = '000'
    else:
        domainname = responsejson['semanticFrames'][0]['domain']['name']
        domainconfidence = responsejson['semanticFrames'][0]['domain']['confidence']
    try:
        responsejson['semanticFrames'][0]["intent"]["code"]
        responsejson['semanticFrames'][0]['intent']['confidence']
    except BaseException:
        intentname = '000'
        intentconfidence = '000'
    else:
        intentname = responsejson['semanticFrames'][0]["intent"]["code"]
        intentconfidence = responsejson['semanticFrames'][0]['intent']['confidence']
    try:
        responsejson['semanticFrames'][0]['subintent']['code']
        responsejson['semanticFrames'][0]['subintent']['confidence']
    except BaseException:
        subintentname = '000'
        subintentconfidence = '000'
    else:
        subintentname = responsejson['semanticFrames'][0]['subintent']['code']
        subintentconfidence = responsejson['semanticFrames'][0]['subintent']['confidence']

    # if ((domainname !='000')&(domainconfidence !='000')&(intentname !='000')&(intentconfidence != '000')&(subintentname !='000')&(subintentconfidence !='000')):
    #     return [domainname,domainconfidence,intentname,intentconfidence,subintentname,subintentconfidence]
    return [domainname,domainconfidence,intentname,intentconfidence,subintentname,subintentconfidence]


if __name__ == '__main__':
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    table.write(0, 0, 'ID')
    table.write(0, 1, '用户问题')
    table.write(0, 2, 'domain')
    table.write(0, 3, 'domainconfidence')
    table.write(0, 4, 'intent')
    table.write(0, 5, 'intentconfidence')
    table.write(0, 6, 'subintent')
    table.write(0, 7, 'subintentconfidence')

    filename = 'D:\\lenovo_data_excel\\201811261206.xlsx'
    sheet = open_files(filename)
    print(sheet.nrows)

    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        print(row[1])
        table.write(i, 0, row[0])
        table.write(i, 1, row[1])
        requestslist = sendjsondata(row[1])
        print(requestslist)
        table.write(i, 2, requestslist[0])
        table.write(i, 3, requestslist[1])
        table.write(i, 4, requestslist[2])
        table.write(i, 5, requestslist[3])
        table.write(i, 6, requestslist[4])
        table.write(i, 7, requestslist[5])

    file.save(r'1126.xls')