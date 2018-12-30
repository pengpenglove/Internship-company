import csv
import pandas
def Entity_word_correspondence_table(filename,word):
    '''
    Find entity word correspondence table,e.g.excel---office
    :param filename:Wordsubstitutiontable.csv
    :param
    :return:corresponding word  or old word
    '''
    with open(filename) as f:
       reader = csv.reader(f)
       for row in reader:
            # 行号从1开始
            # print(reader.line_num, row)
            if (row[0]==word) :
                return row[1]
    return word


if __name__ == '__main__':
    filename = 'Wordsubstitutiontable.csv'
    word = 'office365'
    new_word=Entity_word_correspondence_table(filename, word)
    print(new_word)
