# _*_coding:utf-8_*_
import chardet
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd
import os

def open_chat_log_files(filepath):
    # 打开csv文件并修改该文件
    df = pd.read_csv(filepath, sep=',', encoding="utf-8",header=[1])
    return df



def Cleaning(chat_log_files,savepath):
    new_df = pd.DataFrame(columns=["userid", "user", "service"])

    df_chat_log = open_chat_log_files(chat_log_files)
    specified_column = df_chat_log[['Chat ID', 'Agent Account', 'Text']]
    for i in range(specified_column.shape[0]):
        ChatID = specified_column.iloc[i, :]['Chat ID']
        specified_column_Text = specified_column.iloc[i, :]['Text']
        specified_column_Agent_Account = specified_column.iloc[i, :]['Agent Account']
        specified_column_Text_split = specified_column_Text.split('\n')
        # print(specified_column_Text_split)
        for j in range(1, len(specified_column_Text_split)):
            sentence = re.findall(r"AM\](.+?)\:", specified_column_Text_split[j])
            if sentence:
                if specified_column_Agent_Account.find(sentence[0]) != -1:
                    new_df = new_df.append({'userid': ChatID, 'user': ' ',
                                            'service': re.sub(r'\[(.+?)\](.+?)\:', "", specified_column_Text_split[j])},
                                           ignore_index=True)
                    # new_df = new_df.append({'userid': ChatID, 'user' : ' ', 'service' : specified_column_Text_split[j]} , ignore_index=True)
                else:
                    new_df = new_df.append(
                        {'userid': ChatID, 'user': re.sub(r'\[(.+?)\](.+?)\:', "", specified_column_Text_split[j]),
                         'service': ' '},
                        ignore_index=True)

            else:
                new_df = new_df.append(
                    {'userid': ChatID, 'user': re.sub(r'\[(.+?)\](.+?)\:', "", specified_column_Text_split[j]),
                     'service': ' '}, ignore_index=True)

    writer = pd.ExcelWriter(savepath)
    new_df.to_excel(writer, 'Sheet1')
    writer.save()


def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        save_path = 'D:/lenovo_data_excel/lena/chatlog/222/'
        save_temp_path = os.path.join(save_path, f1.replace(".csv",".xlsx"))
        tmp_path = os.path.join(f, f1)#路径拼接
        if not os.path.isdir(tmp_path):
            print('文件: %s' % tmp_path)
            print(save_temp_path)
            # df_chat_log = open_chat_log_files(tmp_path)
            Cleaning(tmp_path,save_temp_path)
        else:
            print('文件夹：%s' % tmp_path)
            # traverse(tmp_path)


if __name__ == '__main__':
    # chat_log_files = r'D:\lenovo_data_excel\lena\chatlog\1\05.01-05.04.csv'
    # savepath = r'D:/lenovo_data_excel/lena/chatlog/1/output1.xlsx'
    # Cleaning(chat_log_files,savepath)



    path = 'D:/lenovo_data_excel/lena/chatlog/1/22/'
    traverse(path)

