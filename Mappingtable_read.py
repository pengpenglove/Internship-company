# _*_coding:utf-8_*_
'''
本替换文件今适用于KG.csv
'''
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd


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


def lable_replace(file, word, lable):
    csv_data = pd.read_csv(file)  # 读取训练数据
    return Entity_word_correspondence_table(csv_data, word, lable)

if __name__ == '__main__':
    lll=lable_replace(r'D:\lenovo_data_excel\rubi\kg_code_new.csv','How to','Domain')
    print(lll)