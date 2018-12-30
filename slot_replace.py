import csv
import pandas as pd

def Entity_word_correspondence_table(csv_data,word):
    alist =csv_data[csv_data['old L2 intent'] == word].iloc[0, 1]
    print(alist)
    # print(" ".join('%s' % id for id in list(alist['Intent Code'])))
    return alist


if __name__ == '__main__':
    filename = 'D:\\lenovo_data_excel\\rubi\\KG.csv'
    word = 'lync share'
    csv_data = pd.read_csv(filename)  # 读取训练数据
    # print(csv_data.loc[1])
    new_word=Entity_word_correspondence_table(csv_data, word)
    print(new_word)