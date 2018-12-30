'''
rubby
'''
# _*_coding:utf-8_*_
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd
import chardet


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

    # if ((domainname !='000')&(domainconfidence !='000')&(intentname !='000')&(intentconfidence != '000')&(subintentname !='000')&(subintentconfidence !='000')):
    #     return [domainname,domainconfidence,intentname,intentconfidence,subintentname,subintentconfidence]
    return [domainname,domainconfidence,intentname,intentconfidence,subintentname,subintentconfidence]

def Entity_word_correspondence_table(csv_data,word,lable):
    '''
    :param csv_data: KG.csv or others
    :param word: Data corresponding to the label
    :param lable:
    :return:Return according to different labels
    '''
    alist=csv_data.loc[csv_data[lable] == word]
    # alist = csv_data.loc[csv_data['subIntent Code'] == word]

    if lable == 'sub_intent_code':
        # print((" ".join('%s' % id for id in list(alist.iloc[:, 0]))))
        return (" ".join('%s' % id for id in list(alist.iloc[:, 0])))
    if lable == 'intent2':
        # print(type(alist.iloc[1, 1]))
        # return (alist.iloc[1, 1])
        return (alist.iloc[1,3])
    if lable == 'Domain':
        # print(type(alist.iloc[1, 1]))
        # return (alist.iloc[1, 1])
        return (alist.iloc[1,1])

def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


if __name__ == '__main__':


    domainnumber = 0
    intentnumber = 0
    subintentnumber = 0
    jishu0=0
    jishu1=0

    csv_data = pd.read_csv(r'D:\lenovo_data_excel\rubi\kg_code_new.csv')  # 读取训练数据

    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    table.write(0, 0, 'ID')
    table.write(0, 1, '用户问题')
    table.write(0, 2, 'domain')
    table.write(0, 3, 'Original_domainname')
    table.write(0, 4, 'intent')
    table.write(0, 5, 'original_intent')
    table.write(0, 6, 'subintent')
    table.write(0, 7, 'original_subintent')
    table.write(0, 8, 'domaindifference')
    table.write(0, 9, 'intentdifference')
    table.write(0, 10, 'subintentdifference')

    filename = 'D:\\lenovo_data_excel\\rubi\\time1214.xlsx'


    # encoding = get_encoding(filename)
    # print(encoding)

    sheet = open_files(filename)
    print(sheet.nrows)
    for i in range(640,sheet.nrows):
        row = sheet.row_values(i)
        print(row[1])
        table.write(i, 0, row[0])
        table.write(i, 1, row[1])
        table.write(i, 3, row[2])
        table.write(i, 5, row[3])
        table.write(i, 7, row[4])

        words = row[1].split()
        n_words = len(words)
        if n_words > 1 :
            jishu0 = jishu0 +1
            
            requestslist = sendjsondata(row[1])
            # requestslist[2] = Entity_word_correspondence_table(csv_data, requestslist[2], 'intent2')
            requestslist[4] = Entity_word_correspondence_table(csv_data, requestslist[4], 'sub_intent_code')
            print(requestslist)
            table.write(i, 2, requestslist[0])
            table.write(i, 4, requestslist[2])
            table.write(i, 6, requestslist[4])

            if row[2] == requestslist[0]:
                domainnumber = domainnumber + 1
                table.write(i, 8, '1')
            else:
                table.write(i, 8, '0')

            if row[3] == requestslist[2]:
                intentnumber = intentnumber + 1
                table.write(i, 9, '1')
            else:
                table.write(i, 9, '0')

            if row[4] == requestslist[4]:
                table.write(i, 10, '1')
                subintentnumber = subintentnumber + 1
            else:
                table.write(i, 10, '0')
        else:
            jishu1 = jishu1 + 1
            # print(row[1])
            print(n_words)


    print('domainnumber:',domainnumber)
    print('intentnumber:', intentnumber)
    print('subintentnumber',subintentnumber)
    print(jishu0)
    print(jishu1)
    file.save(r'example_test2.xls')