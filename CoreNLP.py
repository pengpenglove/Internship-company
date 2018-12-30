#英文中的应用
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'C:\Users\sunpeng13\PycharmProjects\CoreNLPtest\stanford-corenlp-full-2018-10-05')

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print ("词语分")
print ('Tokenize:', nlp.word_tokenize(sentence))
print ("pos_tag")
print ('Part of Speech:', nlp.pos_tag(sentence))
print ("ner")
print ('Named Entities:', nlp.ner(sentence))
print ("语法树")
print ('Constituency Parsing:', nlp.parse(sentence))#语法树
print("依存句法")
print ('Dependency Parsing:', nlp.dependency_parse(sentence))#依存句法
nlp.close() # Do not forget to close! The backend server will consume a lot memery