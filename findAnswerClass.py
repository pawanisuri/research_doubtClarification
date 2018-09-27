# import xml.etree.ElementTree as ET
# import re
# from xml.dom.minidom import parse, Node
# from test2 import sim
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# from gensim.summarization.textcleaner import split_sentences
# from gensim.summarization import summarize

# from stringMatching import is_ci_token_stopword_set_match
# xmlFile = parse("SRSDocument-Learning tool.xml")
class findAnswerClass:
    def test(self,adss):
        return adss

    # def findAnswer(self,XmlDocumentset,startPage,endPage,keywords):
    #     extractedSentences=[None]*10000
    #     txt = ""
    #     status="notFound"
    #     filtered_sentence1 = []
    #     text=""
    #     # tree = ET.parse(xmlFile)
    #     h="DoCO:SectionTitle"
        
    #     for XmlDocument in XmlDocumentset:     
    #         xmlFile = parse(XmlDocument)   
    #         if(xmlFile.getElementsByTagName("h1")!=[]):
    #             j=0
    #             i=0
    #             for node1 in xmlFile.getElementsByTagName("h1"):
    #                 x = xmlFile.getElementsByTagName("h1")
    #                 txt=x[j].getAttribute('class') 
    #                 if(txt==h):
    #                     for node2 in node1.childNodes:
    #                         if(node2.nodeType == Node.TEXT_NODE) :
    #                             i=i+1
    #                             if(sim(keywords,node2.data.encode("utf-8"))==1):
    #                                 idNo=x[j].getAttribute('id')
    #                                 no=int(idNo)
    #                                 no=no+1
    #                                 idNumber=str(no)
    #                                 # print(idNumber)
    #                                 r=0
    #                                 for f in xmlFile.getElementsByTagName("region"):
    #                                     y = xmlFile.getElementsByTagName("region")
    #                                     Tags=y[r].getAttribute('id') 
    #                                     r=r+1
    #                                     for tages2 in f.childNodes:
    #                                         if(Tags==idNumber):
    #                                             no=no+1
    #                                             idNumber=str(no)
    #                                             print(tages2.data.encode("utf-8"))
    #                                             text=tages2.data.encode("utf-8")
    #                                             filtered_sentence1.append(tages2.data.encode("utf-8"))
    #                                 for node1 in xmlFile.nodeName:
    #                                     # for(i = 0; i < x.length; i=i+1 ){ 
    #                                     txt2=x[j].getAttribute('id')
    #                                     if(txt2=='6'):
    #                                         print("pawi")         
    #                 j=j+1
    #             # summarizationProcess(text)    
    #         if(xmlFile.getElementsByTagName("h2")!=[]):
    #             j=0
    #             i=0
    #             for node1 in xmlFile.getElementsByTagName("h2"):
    #                 x = xmlFile.getElementsByTagName("h2")
    #                 txt=x[j].getAttribute('class') 
    #                 if(txt==h):
    #                     for node2 in node1.childNodes:
    #                         if(node2.nodeType == Node.TEXT_NODE) :
    #                             i=i+1
    #                             if(sim(keywords,node2.data.encode("utf-8"))==1):
    #                                 idNo=x[j].getAttribute('id')
    #                                 no=int(idNo)
    #                                 no=no+1
    #                                 idNumber=str(no)
    #                                 # print(idNumber)
    #                                 r=0
    #                                 for f in xmlFile.getElementsByTagName("region"):
    #                                     y = xmlFile.getElementsByTagName("region")
    #                                     Tags=y[r].getAttribute('id') 
    #                                     # tages2=Tags.childNodes
    #                                     r=r+1
    #                                     for tages2 in f.childNodes:
    #                                         # print("heloowwwwwwwwwwwwww",tages2)    
    #                                         if(Tags==idNumber):
    #                                             img=f.getAttribute('class')
    #                                             if(img=="DoCO:FigureBox"):
    #                                                 print("Image", img)
    #                                             no=no+1
    #                                             idNumber=str(no)
    #                                             # print("Image",qw)
    #                                             print(tages2.data.encode("utf-8"))
    #                                             text=tages2.data.encode("utf-8")
    #                                             filtered_sentence1.append(tages2.data.encode("utf-8"))
    #                                 for node1 in xmlFile.nodeName:
    #                                     # for(i = 0; i < x.length; i=i+1 ){ 
    #                                     txt2=x[j].getAttribute('id')
    #                                     if(txt2=='6'):
    #                                         print("pawi")         
    #                 j=j+1
    #         if(xmlFile.getElementsByTagName("h3")!=[]):
    #             j=0
    #             i=0
    #             for node1 in xmlFile.getElementsByTagName("h3"):
    #                 x = xmlFile.getElementsByTagName("h3")
    #                 txt=x[j].getAttribute('class') 
    #                 if(txt==h):
    #                     for node2 in node1.childNodes:
    #                         if(node2.nodeType == Node.TEXT_NODE) :
    #                             i=i+1
    #                             if(sim(keywords,node2.data.encode("utf-8"))==1):
    #                                 idNo=x[j].getAttribute('id')
    #                                 no=int(idNo)
    #                                 no=no+1
    #                                 idNumber=str(no)
    #                                 # print(idNumber)
    #                                 r=0
    #                                 for f in xmlFile.getElementsByTagName("region"):
    #                                     y = xmlFile.getElementsByTagName("region")
    #                                     Tags=y[r].getAttribute('id') 
    #                                     # tages2=Tags.childNodes
    #                                     r=r+1
    #                                     # print(Tags)
    #                                     for tages2 in f.childNodes:
    #                                         if(Tags==idNumber):
    #                                             no=no+1
    #                                             idNumber=str(no)
    #                                             print(tages2.data.encode("utf-8"))
    #                                             text=tages2.data.encode("utf-8")
    #                                             filtered_sentence1.append(tages2.data.encode("utf-8"))
    #                                 for node1 in xmlFile.nodeName:
    #                                     # for(i = 0; i < x.length; i=i+1 ){ 
    #                                     txt2=x[j].getAttribute('id')
    #                                     if(txt2=='6'):
    #                                         print("pawi")         
    #                 j=j+1         
    #         if(xmlFile.getElementsByTagName("outsider")!=[]):   
    #             j=0 
    #             i=0
    #             for node1 in xmlFile.getElementsByTagName("outsider"):
    #                 x = xmlFile.getElementsByTagName("outsider")
    #                 txt=x[j].getAttribute('class') 
    #                 if(txt=='DoCO:TextBox'):
    #                     for node2 in node1.childNodes:
    #                         if(node2.nodeType == Node.TEXT_NODE) :
    #                             i=i+1
    #                             if(sim(keywords,node2.data.encode("utf-8"))==1):
    #                                 idNo=x[j].getAttribute('id')
    #                                 no=int(idNo)
    #                                 no=no+1
    #                                 idNumber=str(no)
    #                                 # print(idNumber)
    #                                 r=0
    #                                 for f in xmlFile.getElementsByTagName("region"):
    #                                     y = xmlFile.getElementsByTagName("region")
    #                                     Tags=y[r].getAttribute('id') 
    #                                     # tages2=Tags.childNodes
    #                                     r=r+1
    #                                     # print(Tags)
    #                                     for tages2 in f.childNodes:
    #                                         if(Tags==idNumber):
    #                                             print(tages2.data.encode("utf-8"))
    #                                             text=tages2.data.encode("utf-8")
    #                                             filtered_sentence1.append(tages2.data.encode("utf-8"))
    #                                 for node1 in xmlFile.nodeName:
    #                                     # for(i = 0; i < x.length; i=i+1 ){ 
    #                                     txt2=x[j].getAttribute('id')
    #                                     if(txt2=='6'):
    #                                         print("pawi")         
    #                 j=j+1
    #             # summarizationProcess(text)
    #     if(text==""):
    #         print('Informaation Not Found!!!')
    #     else:
    #         print('found!!!')      
    #             # jk=filtered_sentence1
    #         jk=' '.join(filtered_sentence1)
    #             # print(jk) 
        
    #     sentence=split_sentences(jk)
    #     # print(sentence)
    #     sentCount=0
    #     for line in sentence:
    #         sentCount=sentCount+1
    #     # print("Count : zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",sentCount)    
    #     if(sentCount>10):
    #         summarizedText=summarize(extractedInfo, split=True)
    #         return summarizedText
    #     else:
    #         return extractedInfo
    #         summarizationProcess(jk,jk)  
