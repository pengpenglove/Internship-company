# _*_coding:utf-8_*_
# import gensim
import spacy

#打开文件
def openfile(filepath):
    workbook = xlrd.open_workbook(filepath)
    sheet1 = workbook.sheets()[0]
    sheet_col = sheet1.col_values(2)
    return sheet_col,workbook

# nlp = en_core_web_sm.load()
# doc = nlp(u'This is a sentence.')

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_md')
    apple = nlp.vocab[u'apple']
    orange = nlp.vocab[u'orange']
    apple_orange = apple.similarity(orange)
    orange_apple = orange.similarity(apple)
    print(apple_orange == orange_apple)




