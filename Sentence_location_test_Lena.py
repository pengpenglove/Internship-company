# _*_coding:utf-8_*_
import chardet
import xlrd
import xlwt
import re
import sys
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd
sys.path.insert(0, r'C:\Users\sunpeng13\PycharmProjects\CoreNLPtest')
import test_tool_Lena_modify as ttlm
import re
import label_replace_Lena as lrl

def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def open_chat_sentence_files(filepath):
    # 打开csv文件并修改该文件
    df = pd.read_csv(filepath, sep=',', encoding="Windows-1252")
    df_use = df[['userid', 'user']]
    df_userdropna = df_use.dropna()
    # print(df_userdropna.loc[1:2])
    return df_userdropna

def open_chat_log_files(filepath):
    # 打开csv文件并修改该文件
    df = pd.read_csv(filepath, sep=',', encoding="ISO-8859-1")
    return df

def creat_file():
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    table.write(0, 0, 'userid')
    table.write(0, 1, 'user_question')
    table.write(0, 2, 'original_intent')
    return file,table

def write_table(newfile,new_table,new_userid,new_user_question,new_original_intent,number):
    new_table.write(number, 0, new_userid)
    new_table.write(number, 1, new_user_question)
    new_table.write(number, 2, new_original_intent)




if __name__ == '__main__':
    chat_sentence_files = r'D:\\lenovo_data_excel\\lena\\query filter\\test_report_clean1120-8.csv'
    chat_log_files = r'D:\lenovo_data_excel\lena\query filter\chatbot test report pie chart 20181120.csv'
    labelcode = r'D:\lenovo_data_excel\lena\query filter\labelcode.csv'

    newfile,table1 = creat_file()
    encoding = get_encoding(chat_sentence_files)
    print(encoding)
    numberflag = 1
    flag = 0
    #标签替换文件
    label = pd.read_csv(labelcode)

    #长对话
    df_chat_log = open_chat_log_files(chat_log_files)
    # print(df_chat_log[df_chat_log['userid'] == 'SPECSIM@GMAIL.COM'])

    df_chat_user_sentence = open_chat_sentence_files(chat_sentence_files)
    # print(df_chat_user_sentence.loc[1,:])
    # number =df_chat_user_sentence.shape[0]
    for i in range(1,df_chat_user_sentence.shape[0]):
        flag = 0
        userid = df_chat_user_sentence.iloc[i,:].userid
        user = df_chat_user_sentence.iloc[i,:].user
        df_chat_log_one = df_chat_log[df_chat_log['userid'] == userid]
        originalintent = df_chat_log_one.loc[:,'If  no, correct Domain']
        originalintentlabelreplace = lrl.Entity_word_correspondence_table(label, " ".join(
                '%s' % id for id in list(originalintent)).lower(), 'old L3 intent')
        # print('userid:', userid)
        # print('user:',user)
        # print('originalsubintent:'," ".join('%s' % id for id in list(originalintent)))
        # print('originalsubintentlabelreplace:',lrl.Entity_word_correspondence_table(label, " ".join('%s' % id for id in list(originalintent)).lower(), 'old L3 intent'))

        print('userid:', userid)
        print('user:', user)
        print('originalintent:', " ".join('%s' % id for id in list(originalintent)))
        print('originalintentlabelreplace:', lrl.Entity_word_correspondence_table(label, " ".join(
                '%s' % id for id in list(originalintent)).lower(), 'old L3 intent'))

        requestslist = ttlm.sendjsondata(user)
        if len(requestslist) == 1:
            # if " ".join('%s' % id for id in list(originalintent)).lower() == requestslist[0][2]:
            print('requestslist1:',requestslist[0][2])
            if originalintentlabelreplace == requestslist[0][2]:
                print('1')
                flag = 1
        elif len(requestslist) == 2:
            # if (" ".join('%s' % id for id in list(originalintent)).lower() == requestslist[0][2])|(" ".join('%s' % id for id in list(originalintent)).lower() == requestslist[1][2]):
            print('requestslist2:',requestslist[0][2]+'/'+requestslist[1][2])
            if (originalintentlabelreplace == requestslist[0][2])|(originalintentlabelreplace == requestslist[1][2]):
                print('1')
                flag = 1
        else:
            # if (" ".join('%s' % id for id in list(originalintent)).lower() == requestslist[0][2]) | (
            #         " ".join('%s' % id for id in list(originalintent)).lower() == requestslist[1][2])| (
            #         " ".join('%s' % id for id in list(originalintent)).lower() == requestslist[2][2]):
            print('requestslist3:',requestslist[0][2] + '/' + requestslist[1][2]+ '/' + requestslist[2][2])
            if (originalintentlabelreplace == requestslist[0][2]) | (
                    originalintentlabelreplace == requestslist[1][2])| (
                    originalintentlabelreplace == requestslist[2][2]):
                print('1')
                flag = 1
        if flag == 1:
            numberflag =numberflag + 1
            write_table(newfile,table1,userid,user,originalintentlabelreplace,numberflag)


    print(flag)
    newfile.save(r'example20181120.xls')

