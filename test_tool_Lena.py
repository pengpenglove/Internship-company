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

    # if ((domainname !='000')&(domainconfidence !='000')&(intentname !='000')&(intentconfidence != '000')&(subintentname !='000')&(subintentconfidence !='000')):
    #     return [domainname,domainconfidence,intentname,intentconfidence,subintentname,subintentconfidence]
    # return [domainname0,domainconfidence0,intentname0,intentconfidence0,subintentname0,subintentconfidence0]



if __name__ == '__main__':
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    table.write(0, 0, 'ID')
    table.write(0, 1, '用户问题')
    table.write(0, 2, 'domain')
    table.write(0, 3, 'Original_domain')
    table.write(0, 4, 'intent')
    table.write(0, 5, 'original_intent')
    table.write(0, 6, 'subintent')
    table.write(0, 7, 'original_subintent')
    table.write(0, 8, 'domaindifference')
    table.write(0, 9, 'intentdifference')
    table.write(0, 10, 'subintentdifference')

    filename = 'D:\lenovo_data_excel\Test20181026.xlsx'
    sheet = open_files(filename)
    print('sheet.nrows:',sheet.nrows)
    domainnumber = 0
    intentnumber = 0
    subintentnumber = 0
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        print(row[1])
        table.write(i, 0, row[0])
        table.write(i, 1, row[1])
        table.write(i, 3, row[2])
        table.write(i, 5, row[3])
        table.write(i, 7, row[4])

        requestslist = sendjsondata(row[1])
        if len(requestslist) == 1:
            # print(requestslist)
            table.write(i, 2, requestslist[0][0])
            table.write(i, 4, requestslist[0][2])
            table.write(i, 6, requestslist[0][4])
            if row[2] == requestslist[0][0]:
                table.write(i, 8, '1')
                domainnumber = domainnumber + 1
            else:
                table.write(i, 8, '0')
            if row[3] == requestslist[0][2]:
                intentnumber = intentnumber + 1
                table.write(i, 9, '1')
            else:
                table.write(i, 9, '0')
            if row[4] == requestslist[0][4]:
                subintentnumber = subintentnumber + 1
                table.write(i, 10, '1')
            else:
                table.write(i, 10, '0')
        elif len(requestslist) == 2 :
            # print('2:',i)
            table.write(i, 2, requestslist[0][0]+'/'+requestslist[1][0])
            table.write(i, 4, requestslist[0][2]+'/'+requestslist[1][2])
            table.write(i, 6, requestslist[0][4]+'/'+requestslist[1][4])
            if ((row[2] == requestslist[0][0])|(row[2] == requestslist[1][0])):
                domainnumber = domainnumber + 1
                table.write(i, 8, '1')
            else:
                table.write(i, 8, '0')
            if ((row[3] == requestslist[0][2])|(row[3] == requestslist[1][2])):
                intentnumber = intentnumber + 1
                table.write(i, 9, '1')
            else:
                table.write(i, 9, '0')
            if ((row[4] == requestslist[0][4])|(row[4] == requestslist[1][4])):
                subintentnumber = subintentnumber + 1
                table.write(i, 10, '1')
            else:
                table.write(i, 10, '0')

        else:
            # print('3:',i)
            table.write(i, 2, requestslist[0][0] + '/' + requestslist[1][0]+ '/' + requestslist[2][0])
            table.write(i, 4, requestslist[0][2] + '/' + requestslist[1][2]+'/' + requestslist[2][2])
            table.write(i, 6, requestslist[0][4] + '/' + requestslist[1][4]+ '/' + requestslist[2][4])
            if ((row[2] == requestslist[0][0]) | (row[2] == requestslist[1][0])| (row[2] == requestslist[2][0])):
                table.write(i, 8, '1')
                domainnumber = domainnumber + 1
            else:
                table.write(i, 8, '0')
            if ((row[3] == requestslist[0][2]) | (row[3] == requestslist[1][2])| (row[3] == requestslist[2][2])):
                intentnumber = intentnumber + 1
                table.write(i, 9, '1')
            else:
                 table.write(i, 9, '0')
            if ((row[4] == requestslist[0][4]) | (row[4] == requestslist[1][4])| (row[4] == requestslist[2][4])):
                subintentnumber = subintentnumber + 1
                table.write(i, 10, '1')
            else:
                table.write(i, 10, '0')
    print('domainnumber:',domainnumber)
    print('intentnumber:', intentnumber)
    print('subintentnumber',subintentnumber)
    file.save(r'example_test3.xls')







