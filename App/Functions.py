from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import nltk
word_lemitizer = WordNetLemmatizer()

Regular_expression_definition_for_html_tags=re.compile('<.*?>')
Regular_expression_definition_for_digits=re.compile('\d+\s|\s\d+|\s\d+\s')
Regular_expression_definition_for_links=re.compile('http://\S+|https://\S+')
class WordLevelDetection:
    def __init__(self,word):
        self.word=word
    def detectlanguage(self):
        counter = 0
        for i in self.word:
            if ord(i) >= 65 and ord(i) <= 123 or ord(i)>=48 and ord(i)<=57:
                counter = counter + 1
        if counter == len(self.word):
            return True
        return False
    def getWord(self):
        return(self.word)

class SentenceLevelDetection(WordLevelDetection):
    def __init__(self, sentence):
        self.sentence = sentence
    def preprocessing(self):
        self.word = self.sentence.lower()
        # self.word= "".join(self.word)        
        for i in [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']:
            self.word = self.word.replace(i," ")
        self.word=self.word.split()
        self.word= "".join(self.word)

def scriptValidation(text):
    text=Regular_expression_definition_for_html_tags.sub(r" ",text)
    text=Regular_expression_definition_for_links.sub(r" ",text)
    text=Regular_expression_definition_for_digits.sub(r" ",text)
    sentenceLevelDetection=SentenceLevelDetection(text);
    sentenceLevelDetection.preprocessing()
    print(sentenceLevelDetection.getWord())
    return sentenceLevelDetection.detectlanguage()

def filtaration(text):
    text=Regular_expression_definition_for_html_tags.sub(r" ",text)
    text=Regular_expression_definition_for_links.sub(r" ",text)
    text=Regular_expression_definition_for_digits.sub(r" ",text)
    punctuations = [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']
    for i in punctuations:
        text = text.replace(i," ")
    temp_text=""
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 123:
            temp_text+=i
        if ord(i)==32:
            temp_text+=" "
    text=temp_text
    text=text.lower()
    return text

english_stop_words=stopwords.words('english')

def Tokenization(text):
    text=Regular_expression_definition_for_html_tags.sub(r" ",text)
    text=Regular_expression_definition_for_links.sub(r" ",text)
    text=Regular_expression_definition_for_digits.sub(r" ",text)
    punctuations = [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']
    for i in punctuations:
        text = text.replace(i," ")
    temp_text=""
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 123:
            temp_text+=i
        if ord(i)==32:
            temp_text+=" "
    text=temp_text
    text=text.lower().split()
    text=[word for word in text if len(word)>1 and word not in english_stop_words]
    return text


def Lemmitization(text):
    text=Regular_expression_definition_for_html_tags.sub(r" ",text)
    text=Regular_expression_definition_for_links.sub(r" ",text)
    text=Regular_expression_definition_for_digits.sub(r" ",text)
    punctuations = [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']
    for i in punctuations:
        text = text.replace(i," ")
    temp_text=""
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 123:
            temp_text+=i
        if ord(i)==32:
            temp_text+=" "
    text=temp_text
    text=text.lower().split()
    text=[word for word in text if len(word)>1 and word not in english_stop_words]
    text = [word_lemitizer.lemmatize(word) for word in text]
    return text

def pos_Tagging(text):
    text=Regular_expression_definition_for_html_tags.sub(r" ",text)
    text=Regular_expression_definition_for_links.sub(r" ",text)
    text=Regular_expression_definition_for_digits.sub(r" ",text)
    punctuations = [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']
    for i in punctuations:
        text = text.replace(i," ")
    temp_text=""
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 123:
            temp_text+=i
        if ord(i)==32:
            temp_text+=" "
    text=temp_text
    text=text.lower().split()
    text=[word for word in text if len(word)>1 and word not in english_stop_words]
    text=nltk.pos_tag(text)
    return text