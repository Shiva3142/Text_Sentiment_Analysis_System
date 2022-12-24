import pickle
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from .Variables import *
import joblib

word_lemitizer = WordNetLemmatizer()
Regular_expression_definition_for_html_tags=re.compile('<.*?>')
Regular_expression_definition_for_digits=re.compile('\d+\s|\s\d+|\s\d+\s')
Regular_expression_definition_for_links=re.compile('http://\S+|https://\S+')
english_stop_words=stopwords.words('english')

class TextInputProcessor:
    def __init__(self):        
        print("""🚀🚀🚀Text input Processor🚀🚀🚀""")
    def setVecorizer(self,path):
        with open(path,"rb") as f:
            self.Vectorizer=pickle.load(f)
    def getPreprocessedInput(self,inputText):
        inputText=Regular_expression_definition_for_html_tags.sub(r" ",inputText)
        inputText=Regular_expression_definition_for_digits.sub(r" ",inputText)
        inputText=Regular_expression_definition_for_links.sub(r" ",inputText)
        punctuations = [".","=","_","<",">",",","!","?","'",'"',":",";","*","-","/","+","%","$","#","@","(",")","[","]","{","}",'\n']
        for i in punctuations:
            inputText = inputText.replace(i," ")
        inputText=inputText.lower().split()
        inputText=[word_lemitizer.lemmatize(word) for word in inputText]
        return inputText

    def getPreprocessTheArray(self,inputText):
        inputText=[ text for text in inputText.split(".") if len(text)>1]
        Processed_Text=[" ".join(self.getPreprocessedInput(sentence)) for sentence in inputText]
        print(Processed_Text)
        return self.Vectorizer.transform(Processed_Text)

    def getVectorArray(self,inputVector):
        final_array=[]
        for j in [i for i in inputVector.toarray()]:
            for k in j:
                final_array.append(k)
        return final_array
    def getVectorizedForm(self,inputText):
        return self.Vectorizer.transform([inputText])


class TextSentimentAnalyser:
    def __init__(self):
        print("""🚀🚀🚀Text input Analyzer🚀🚀🚀""")
    def setModel(self,path):    
        self.model=joblib.load(path)
    def predict(self,inputVector):
        return self.model.predict(inputVector)[0]    
    def getCumulativePrediction(self,inputVector):
        predictions=list(self.model.predict(inputVector))
        unique_value=list(set(predictions))
        max_voted_value=predictions[0]
        max_vote=predictions.count(max_voted_value)
        for i in unique_value:
            if max_vote<predictions.count(i):
                max_voted_value=i
                max_vote=predictions.count(i)
        return max_voted_value
    def getInterMediateCumulativePrediction(self,inputVector):
        predictions=list(self.getArrayofIntermediateEmotions(self.model.predict(inputVector)))
        unique_value=list(set(predictions))
        max_voted_value=predictions[0]
        max_vote=predictions.count(max_voted_value)
        for i in unique_value:
            if max_vote<predictions.count(i):
                max_voted_value=i
                max_vote=predictions.count(i)
        return max_voted_value
    def getTraditionalCumulativePrediction(self,inputVector):
        predictions=list(self.getArrayofSentimentLevelEmotions(self.model.predict(inputVector)))
        unique_value=list(set(predictions))
        max_voted_value=predictions[0]
        max_vote=predictions.count(max_voted_value)
        for i in unique_value:
            if max_vote<predictions.count(i):
                max_voted_value=i
                max_vote=predictions.count(i)
        return max_voted_value
    def getIntermediateEmotions(self,result):
        for key in Intermediate_Grouped_Emotions.keys():
            if result in Intermediate_Grouped_Emotions[key]:
                return key
        return "Neutral"
    def getSentimentLevelEmotions(self,result):
        for key in Sentiment_Level_Grouped_Emotions.keys():
            if result in Sentiment_Level_Grouped_Emotions[key]:
                return key
        return "Neutral"
    def getArrayofIntermediateEmotions(self,result):
        output=[]
        for value in result:
            for key in Intermediate_Grouped_Emotions.keys():
                if value in Intermediate_Grouped_Emotions[key]:
                    output.append(key)
        return output
    def getArrayofSentimentLevelEmotions(self,result):
        output=[]
        for value in result:
            for key in Sentiment_Level_Grouped_Emotions.keys():
                if value in Sentiment_Level_Grouped_Emotions[key]:
                    output.append(key)
        return output
