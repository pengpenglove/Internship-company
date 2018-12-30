# _*_coding:utf-8_*_
import xlrd
import xlwt
import re
from xlutils.copy import copy
import simplejson as json
import requests
import pandas as pd

def open_files():
    # 打开excel文件并修改该文件
    # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
    df = pd.read_csv(r'D:\lenovo_data_excel\Test20181026.csv', header=None,sep=',')
    print(df.loc[:,1])


if __name__ == '__main__':
    open_files()