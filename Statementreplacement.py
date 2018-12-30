from nltk.corpus import wordnet as wn
import nltk
import re
# nltk.download()
# for replaceword in wn.synsets('cat'):
#     print(replaceword)

def replaceword(word):
    """
    Replace the specified word
    :param word:Words to be replaced
    :return List of similar words
    """
    tokenlist=[]
    for synset in list(wn.synsets(word))[:10]:
        tokenlist.append(synset.lemmas()[0].name())
        # print(synset.lemmas()[0].name())
    return tokenlist


def replacesentence(sentence):
    '''
    Sentence replacement
    :param sentence:sentence to be replaced
    :return:List of similar sentence
    '''
    sentencelist=[]
    words = nltk.word_tokenize(sentence)
    word_tag = nltk.pos_tag(words)
    for i in word_tag:

        if ((i[1] == 'RB') | (i[1] == 'VBD') | (i[1] == 'VBG') | (i[1] == 'VBN')):
            newwordlist = replaceword(i[0])
            for newword in newwordlist:
                newsentence = re.sub(i[0], newword, sentence)
                sentencelist.append(newsentence)
        if ((i[1] == 'NN') | (i[1] == 'NNS') | (i[1] == 'NNP') | (i[1] == 'NNPS')):
            newwordlist = replaceword(i[0])
            for newword in newwordlist:
                newsentence = re.sub(i[0], newword, sentence)
                sentencelist.append(newsentence)
    return sentencelist

if __name__ == '__main__':
    sentence = "From the mountain peaks in the east，The silvery moon has peeped out。"
    newsentencelist = replacesentence(sentence)
    print(newsentencelist)