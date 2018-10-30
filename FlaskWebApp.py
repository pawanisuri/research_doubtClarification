from flask import Flask,jsonify,render_template,flash
from findAnswerForQuestion import findAnswer
# from findAnswerClass import findAnswerClass
# from testClass
from chapters import pdf_splitter
from flask import request,url_for,redirect
import re
import json
webapp = Flask(__name__)
# @webapp.route("/")
# def hello():
#  return " Hello World!"

@webapp.route("/")
def hello():
    return jsonify({"status":"1","result":"API is running on:3500"})

@webapp.route("/doubts",methods=['POST'])
def doubts():
    # documents = request.form.getlist('documents')
    # keywords = request.form.getlist('keywords')
    req_data = request.get_json()
    documents=req_data['documents']
    keywords=req_data['keywords']
    # print(documents)
    # for line in documents:
    #     line = line[2:]
    # data = request.data
    # dataDict = json.loads(data)
    # startPage = request.form['startPage'] 
    # endPage = request.form['endPage'] 
    # print("line ",line)
    # keywords = request.form['keywords'] 
    # spage = request.form['spage']
    # epage = request.form['epage']
    # documents=['Data Communication Networking.xml','android_tutorial.xml']
    # keywords=['Summary','Ring Topology']
    # l = documents.split(']')[0]
    # l = l.split('[')[1]
    # l = l.encode("utf-8")
    # l = l.strip('\"')
    # print l

    # ll = keywords.split(']')[0]
    # ll = ll.split('[')[1]
    # ll=ll.encode("utf-8")
    # print ll
    li_u_removed = [str(i) for i in documents]
    li_u_removedss = [str(i) for i in keywords]
    print("asdad",li_u_removed) 
    print(li_u_removedss) 
#    print(a) 
    
    # output = findAnswer([l.replace('"', '')],startPage,endPage,[ll])
    output = findAnswer(documents,keywords)
    # output="Done"
    return jsonify({"status":"1","result":output}) 

# @webapp.route("/doubts123",methods=['POST'])
# def doubts123():
#    XmlDocument = request.form['XmlDocument'] 
#    clsx=findAnswerClass.test(XmlDocument,XmlDocument)
#     # find=clsx.f(0)
#     testC = testClass.testClass()
#     test = testC.f('a')
#     if request.method=="POST":
#         return jsonify({"status":"1","result": test})
#     else:   
#         return jsonify({"status":"0","result":'Error'}) 
@webapp.route("/chapter",methods=['POST'])
def chapter():
    # s = request.form['s']    
    req_data = request.get_json()
    path=req_data['path']
    print(path)
    spage = req_data['spage']
    epage = req_data['epage']
    # path = request.form['path']
    # spage = request.form['spage']
    # epage = request.form['epage']
    pdfoutput=pdf_splitter(path,spage,epage)
    return jsonify({"status":"1","result":pdfoutput})    

if __name__ == '__main__':
 webapp.run(host='104.248.53.134', debug=True)    #port=3500,