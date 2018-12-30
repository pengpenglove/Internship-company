import csv
import pandas as pd

def Entity_word_correspondence_table(csv_data,word):
    # print(csv_data.loc[csv_data['oldword'] == word])
    alist=csv_data.loc[csv_data['oldword'] == word]
    if (" ".join('%s' %id for id in list(alist.iloc[:,1].index))):
        return alist.iloc[:,1]
    # if alist.iloc[:,1]!=word :
    # return list(alist.iloc[:,1].index)
    return word

if __name__ == '__main__':
    filename = 'Wordsubstitutiontable.csv'
    word = 'excel'
    csv_data = pd.read_csv(filename)  # 读取训练数据
    # print(csv_data.loc[1])
    new_word=Entity_word_correspondence_table(csv_data, word)
    print(new_word)