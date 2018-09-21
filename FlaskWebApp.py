from flask import Flask
from findAnswerForQuestion import findAnswer
from chapters import pdf_splitter
from flask import request
webapp = Flask(__name__)
@webapp.route("/")
def hello():
 return " Hello World!"
if __name__ == '__main__':
 webapp.run(host='0.0.0.0',port=8999,debug=True)

@webapp.route("/doubts/question",methods=['POST'])
def findAnswerForQuestion():
    XmlDocument = request.form.get('XmlDocument')    
    startPage = request.form.get('startPage')
    endPage = request.form.get('endPage')
    keywords = request.form.get('keywords')
    return findAnswer(XmlDocument,startPage,endPage,keywords)

@webapp.route("/xmlDocument/chapter",methods=['GET'])
def convertChapters():
    s = request.form.get('s')    
    spage = request.form.get('spage')
    epage = request.form.get('epage')
    return pdf_splitter(s,spage,epage)    