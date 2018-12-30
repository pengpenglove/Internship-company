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
    new_row = new_sheet.row_values(4)
    return new_row, new_sheet

def Entity_word_correspondence_table(csv_data,word):
    # print(csv_data.loc[csv_data['oldword'] == word])
    alist=csv_data.loc[csv_data['subIntent Code'] == word]
    # print(alist.iloc[:,0])
    # return alist.iloc[:,0]
    return (" ".join('%s' % id for id in list(alist.iloc[:, 0])))
    # return alist['Serial-Number'][0]



# def Entity_word_correspondence_table2(csv_data,word):
#     alist =csv_data[csv_data['old L2 intent'] == word].iloc[0, 1]
#     return (" ".join(alist))

if __name__ == "__main__":
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
    table.write(0, 8, 'Original_domainname')
    table.write(0, 9, 'original_intent')
    table.write(0, 10, 'original_Standard_Question')

    filenameKG = 'D:\\lenovo_data_excel\\rubi\\KG.csv'
    csv_data = pd.read_csv(filenameKG)  # 读取训练数据

    filename ='D:/lenovo_data_excel/rubi/Robot_chatlog_en_part1_11.14.xlsx'
    row, sheet = open_files(filename)
    row = sheet.row_values(0)
    i =1  # 行下标

    for i in range(1270,3834):
        row = sheet.row_values(i)
        sentence = row[1]
        Original_domainname=row[2]
        original_intent = row[4]
        original_Standard_Question = row[7]
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

        subintentname = Entity_word_correspondence_table(csv_data, subintentname)
        # intentname = Entity_word_correspondence_table2(csv_data, intentname)

        print(sentence,'domainname:',domainname,'domainconfidence:',domainconfidence,'intentname:',intentname,'intentconfidence:',intentconfidence,'subintentname',subintentname,'subintentconfidence:',subintentconfidence)
        # print("Original_domainname:",Original_domainname,"original_intent:",original_intent,"original_Standard_Question:",original_Standard_Question)
        table.write(i, 0, row[0])
        table.write(i, 1, row[1])
        table.write(i, 2, domainname)
        table.write(i, 3, domainconfidence)
        table.write(i, 4, intentname)
        table.write(i, 5, intentconfidence)
        table.write(i, 6, subintentname)
        table.write(i, 7, subintentconfidence)
        table.write(i, 8, Original_domainname)
        table.write(i, 9, original_intent)
        table.write(i, 10,original_Standard_Question)

    file.save(r'example1.xls')

