# _*_coding:utf-8_*_
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests

def open_files(filepath):
    # 打开excel文件并修改该文件
    new_content = xlrd.open_workbook(filepath,encoding_override="utf-8")
    new_sheet = new_content.sheets()[0]
    new_row = new_sheet.row_values(4)
    return new_row, new_sheet

if __name__ == "__main__":
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    table.write(0, 0, '用户问题')
    table.write(0, 1, 'domain')
    table.write(0, 2, 'domainconfidence')
    table.write(0, 3, 'intent')
    table.write(0, 4, 'intentconfidence')
    table.write(0, 5, 'subintent')
    table.write(0, 6, 'subintentconfidence')

    filename ='D:/lenovo_data_excel/rubi/log_1.xlsx'
    row, sheet = open_files(filename)
    row = sheet.row_values(0)
    i =1  # 行下标

    for i in range(1,1225):
        row = sheet.row_values(i)
        sentence = row[0]
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
        url = 'http://192.168.3.9:21000'
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

        # print(sentence,'domainname:',domainname,'domainconfidence:',domainconfidence,'intentname:',intentname,'intentconfidence:',intentconfidence,'subintentname',subintentname,'subintentconfidence:',subintentconfidence)
        table.write(i, 0, row[0])
        table.write(i, 1, domainname)
        table.write(i, 2, domainconfidence)
        table.write(i, 3, intentname)
        table.write(i, 4, intentconfidence)
        table.write(i, 5, subintentname)
        table.write(i, 6, subintentconfidence)

    file.save(r'Beforehand marking.xls')

