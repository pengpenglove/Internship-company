# _*_coding:utf-8_*_
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

    if lable == 'old L3 intent':
        # print((" ".join('%s' % id for id in list(alist.iloc[:, 0]))))
        return (" ".join('%s' % id for id in list(alist.iloc[:, 1])))





if __name__ == '__main__':
    labelcode = r'D:\lenovo_data_excel\lena\query filter\labelcode.csv'
    label = pd.read_csv(labelcode)
    sentence = 'Warranty Date Update and Registration'
    print(Entity_word_correspondence_table(label,sentence.lower(),'old L3 intent'))