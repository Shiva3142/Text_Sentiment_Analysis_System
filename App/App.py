from flask import Flask,render_template,request,jsonify
import os
from Model.TextProcessor import *
from Functions import *

textInputProcessor=TextInputProcessor()
textInputProcessor.setVecorizer("../Model/Vectorizer.pickle")
textSentimentAnalyser=TextSentimentAnalyser()
textSentimentAnalyser.setModel("../Model/Model.joblib")
App=Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/getresult',methods=['POST','GET'])
def getfinalresult():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            print(request.json['text'])
            filtered=filtaration(request.json['text'])
            tokenized=Tokenization(request.json['text'])
            lemmetized=Lemmitization(request.json['text'])
            POSTagged=pos_Tagging(request.json['text'])
            input_=textInputProcessor.getPreprocessTheArray(request.json['text'])
            print("Preprocessed_input : ", input_)
            prediction=textSentimentAnalyser.getInterMediateCumulativePrediction(input_)
            generalizedPrediction=textSentimentAnalyser.getTraditionalCumulativePrediction(input_)
            specificPrediction=textSentimentAnalyser.predict(input_)
            print(prediction)
            return jsonify({
                "sentiment":prediction,
                "filtered":filtered,
                "tokenized":tokenized,
                "lemmetized":lemmetized,
                "POSTagged":POSTagged,
                "generalizedPrediction":generalizedPrediction,
                "specificPrediction":specificPrediction
                })
    else:
        return jsonify({"data":"ERROR"})

@App.route('/validate',methods=['POST','GET'])
def getValidation():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        # print(request.json['text'])
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            value=scriptValidation(request.json['text'])
            print(value)
            if value==True:
                return jsonify({"data":"Valid"})
            else:
                return jsonify({"data":"Invalid"})
    else:
        return jsonify({"data":"ERROR"})

@App.route('/filterthetext',methods=['POST','GET'])
def getFiltration():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        # print(request.json['text'])
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            value=filtaration(request.json['text'])
            print(value)
            return jsonify({"data":value})
    else:
        return jsonify({"data":"ERROR"})
@App.route('/tokenize',methods=['POST','GET'])
def getTokens():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        # print(request.json['text'])
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            value=Tokenization(request.json['text'])
            print(value)
            returningvalue="[ "
            for i in value:
                returningvalue+=f" {i} , "
            returningvalue+=" ]"
            return jsonify({"data":returningvalue})
    else:
        return jsonify({"data":"ERROR"})

@App.route('/lemmetization',methods=['POST','GET'])
def getStems():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        # print(request.json['text'])
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            value=Lemmitization(request.json['text'])
            print(value)
            returningvalue="[ "
            for i in value:
                returningvalue+=f" {i} , "
            returningvalue+=" ]"
            return jsonify({"data":returningvalue})
    else:
        return jsonify({"data":"ERROR"})

@App.route('/postagging',methods=['POST','GET'])
def getPOStags():
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        # print(request.json['text'])
        if request.json['text']=="":
            return jsonify({"data":"ERROR"})
        else:
            value=pos_Tagging(request.json['text'])
            print(value)
            returningvalue="[ "
            for i in value:
                returningvalue+=f" {i} , "
            returningvalue+=" ]"
            return jsonify({"data":returningvalue})
    else:
        return jsonify({"data":"ERROR"})

@App.route('/upload',methods=['POST','GET'])
def upload():
    global file_name
    if request.method=='POST':
        print(request.files['file'])
        # print(request.files)
        file=request.files['file']
        file_name=file.filename
        extension=file_name.split(".")[-1]
        file_name=f"input.{extension}"
        print(file_name)
        file.filename=file_name
        print(file)
        file.save(os.path.dirname(__file__)+f"\\static\\data\\files\\{file_name}")
        with open("./static/data/files/input.txt") as f:
            text_data=f.read()
        return jsonify({"data":text_data})
    else:
        return "error"