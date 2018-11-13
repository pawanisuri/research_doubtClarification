import xml.etree.ElementTree as ET
import re
from xml.dom.minidom import parse, Node
from test2 import sim
from sum import summary

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization.textcleaner import split_sentences
from gensim.summarization import summarize

# from stringMatching import is_ci_token_stopword_set_match
# xmlFile = parse("SRSDocument-Learning tool.xml")
filtered_sentence1 = []
def findAnswer(XmlDocumentset,keywords):
    extractedSentences=[None]*1000000
    txt = ""
    state="not found"
    status="notFound"
    
    text=""
    # tree = ET.parse(xmlFile)
    h="DoCO:SectionTitle"
    
    for XmlDocument in XmlDocumentset:   
        print("xml Document",XmlDocument)  
        xmlFile = parse(XmlDocument)   
        if(xmlFile.getElementsByTagName("region")!=[]):
            j=0
            i=0
            for node1 in xmlFile.getElementsByTagName("region"):
                x = xmlFile.getElementsByTagName("region")
                txt=x[j].getAttribute('class') 
                if(txt=='unknown'):
                    for node2 in node1.childNodes:
                        if(node2.nodeType == Node.TEXT_NODE) :
                            i=i+1
                            ww=node2.data.encode('utf-8')
                            # print(ww)
                            if(sim(keywords,ww)==1):
                                idNumber=x[j].getAttribute('id')
                                print(idNumber)
                                while state != 'found':
                                    no=int(idNumber)
                                    no=no+1
                                    idNumber=str(no)
                                    print("id no " ,idNumber)
                                    r=0
                                    # xmlFile = parse(XmlDocument) 
                                    for f in xmlFile.getElementsByTagName("region"):
                                        y = xmlFile.getElementsByTagName("region")
                                        Tags=y[r].getAttribute('id') 
                                        r=r+1
                                        for tages2 in f.childNodes:
                                            if(Tags==idNumber):
                                                no=no+1
                                                idNumber=str(no)
                                                print(tages2.data.encode("utf-8"))
                                                text=tages2.data.encode("utf-8")
                                                filtered_sentence1.append(tages2.data.encode("utf-8"))
                                                state="found"
                                    
                                        # for f in xmlFile.getElementsByTagName("region"):
                                        #     y = xmlFile.getElementsByTagName("region")
                                        #     Tags=y[r].getAttribute('id') 
                                        #     r=r+1
                                        # for tages2 in f.childNodes:
                                        #     if(Tags==idNumber):
                                        #         no=no+1
                                        #         idNumber=str(no)
                                        #         print(tages2.data.encode("utf-8"))
                                        #         text=tages2.data.encode("utf-8")
                                        #         filtered_sentence1.append(tages2.data.encode("utf-8"))
                                        #         state="found"
                                        # no=int(idNumber)
                                        # no=no+1
                                        # idNumber=str(no)
                                        # print("NOt found ",idNumber)
                                        # getInfo(XmlDocument,r,idNumber,no)                    
                                for node1 in xmlFile.nodeName:
                                    txt2=x[j].getAttribute('id')
                                    if(txt2=='6'):
                                        print("pawi")         
                j=j+1

        if(xmlFile.getElementsByTagName("h1")!=[]):
            j=0
            i=0
            for node1 in xmlFile.getElementsByTagName("h1"):
                x = xmlFile.getElementsByTagName("h1")
                txt=x[j].getAttribute('class') 
                if(txt==h):
                    for node2 in node1.childNodes:
                        if(node2.nodeType == Node.TEXT_NODE) :
                            i=i+1
                            if(sim(keywords,node2.data.encode("utf-8"))==1):
                                idNo=x[j].getAttribute('id')
                                no=int(idNo)
                                no=no+1
                                idNumber=str(no)
                                # print(idNumber)
                                r=0
                                for f in xmlFile.getElementsByTagName("region"):
                                    y = xmlFile.getElementsByTagName("region")
                                    Tags=y[r].getAttribute('id') 
                                    r=r+1
                                    for tages2 in f.childNodes:
                                        if(Tags==idNumber):
                                            no=no+1
                                            idNumber=str(no)
                                            print(tages2.data.encode("utf-8"))
                                            text=tages2.data.encode("utf-8")
                                            filtered_sentence1.append(tages2.data.encode("utf-8"))
                                for node1 in xmlFile.nodeName:
                                    # for(i = 0; i < x.length; i=i+1 ){ 
                                    txt2=x[j].getAttribute('id')
                                    if(txt2=='6'):
                                        print("pawi")         
                j=j+1        
            # summarizationProcess(text)    
        if(xmlFile.getElementsByTagName("h2")!=[]):
            j=0
            i=0
            for node1 in xmlFile.getElementsByTagName("h2"):
                x = xmlFile.getElementsByTagName("h2")
                txt=x[j].getAttribute('class') 
                if(txt==h):
                    for node2 in node1.childNodes:
                        if(node2.nodeType == Node.TEXT_NODE) :
                            i=i+1
                            if(sim(keywords,node2.data.encode("utf-8"))==1):
                                idNo=x[j].getAttribute('id')
                                no=int(idNo)
                                no=no+1
                                idNumber=str(no)
                                # print(idNumber)
                                r=0
                                for f in xmlFile.getElementsByTagName("region"):
                                    y = xmlFile.getElementsByTagName("region")
                                    Tags=y[r].getAttribute('id') 
                                    # tages2=Tags.childNodes
                                    r=r+1
                                    for tages2 in f.childNodes:
                                        # print("heloowwwwwwwwwwwwww",tages2)    
                                        if(Tags==idNumber):
                                            img=f.getAttribute('class')
                                            if(img=="DoCO:FigureBox"):
                                                print("Image", img)
                                            no=no+1
                                            idNumber=str(no)
                                            # print("Image",qw)
                                            print(tages2.data.encode("utf-8"))
                                            text=tages2.data.encode("utf-8")
                                            filtered_sentence1.append(tages2.data.encode("utf-8"))
                                for node1 in xmlFile.nodeName:
                                    # for(i = 0; i < x.length; i=i+1 ){ 
                                    txt2=x[j].getAttribute('id')
                                    if(txt2=='6'):
                                        print("pawi")         
                j=j+1
        if(xmlFile.getElementsByTagName("h3")!=[]):
            j=0
            i=0
            for node1 in xmlFile.getElementsByTagName("h3"):
                x = xmlFile.getElementsByTagName("h3")
                txt=x[j].getAttribute('class') 
                if(txt==h):
                    for node2 in node1.childNodes:
                        if(node2.nodeType == Node.TEXT_NODE) :
                            i=i+1
                            if(sim(keywords,node2.data.encode("utf-8"))==1):
                                idNo=x[j].getAttribute('id')
                                no=int(idNo)
                                no=no+1
                                idNumber=str(no)
                                # print(idNumber)
                                r=0
                                for f in xmlFile.getElementsByTagName("region"):
                                    y = xmlFile.getElementsByTagName("region")
                                    Tags=y[r].getAttribute('id') 
                                    # tages2=Tags.childNodes
                                    r=r+1
                                    # print(Tags)
                                    for tages2 in f.childNodes:
                                        if(Tags==idNumber):
                                            no=no+1
                                            idNumber=str(no)
                                            print(tages2.data.encode("utf-8"))
                                            text=tages2.data.encode("utf-8")
                                            filtered_sentence1.append(tages2.data.encode("utf-8"))
                                for node1 in xmlFile.nodeName:
                                    # for(i = 0; i < x.length; i=i+1 ){ 
                                    txt2=x[j].getAttribute('id')
                                    if(txt2=='6'):
                                        print("pawi")         
                j=j+1         
        if(xmlFile.getElementsByTagName("outsider")!=[]):   
            j=0 
            i=0
            for node1 in xmlFile.getElementsByTagName("outsider"):
                x = xmlFile.getElementsByTagName("outsider")
                txt=x[j].getAttribute('class') 
                if(txt=='DoCO:TextBox'):
                    for node2 in node1.childNodes:
                        if(node2.nodeType == Node.TEXT_NODE) :
                            i=i+1
                            if(sim(keywords,node2.data.encode("utf-8"))==1):
                                idNumber=x[j].getAttribute('id')
                                while state != 'found':
                                    no=int(idNumber)
                                    no=no+1
                                    idNumber=str(no)
                                    print("id no " ,idNumber)
                                    r=0
                                    # xmlFile = parse(XmlDocument) 
                                    for f in xmlFile.getElementsByTagName("region"):
                                        y = xmlFile.getElementsByTagName("region")
                                        Tags=y[r].getAttribute('id') 
                                        r=r+1
                                        for tages2 in f.childNodes:
                                            if(Tags==idNumber):
                                                no=no+1
                                                idNumber=str(no)
                                                print(tages2.data.encode("utf-8"))
                                                text=tages2.data.encode("utf-8")
                                                filtered_sentence1.append(tages2.data.encode("utf-8"))
                                                state="found"
                                    
                                        # for f in xmlFile.getElementsByTagName("region"):
                                        #     y = xmlFile.getElementsByTagName("region")
                                        #     Tags=y[r].getAttribute('id') 
                                        #     r=r+1
                                        # for tages2 in f.childNodes:
                                        #     if(Tags==idNumber):
                                        #         no=no+1
                                        #         idNumber=str(no)
                                        #         print(tages2.data.encode("utf-8"))
                                        #         text=tages2.data.encode("utf-8")
                                        #         filtered_sentence1.append(tages2.data.encode("utf-8"))
                                        #         state="found"
                                        # no=int(idNumber)
                                        # no=no+1
                                        # idNumber=str(no)
                                        # print("NOt found ",idNumber)
                                        # getInfo(XmlDocument,r,idNumber,no)                    
                                for node1 in xmlFile.nodeName:
                                    txt2=x[j].getAttribute('id')
                                    # if(txt2=='6'):
                                    #      print("pawi") 
                j=j+1

        # if(xmlFile.getElementsByTagName("region")!=[]):   
        #     j=0 
        #     i=0
        #     for node1 in xmlFile.getElementsByTagName("region"):
        #         x = xmlFile.getElementsByTagName("region")
        #         txt=x[j].getAttribute('class') 
        #         if(txt=='unknown'):
        #             for node2 in node1.childNodes:
        #                 if(node2.nodeType == Node.TEXT_NODE) :
        #                     i=i+1
        #                     if(sim(keywords,node2.data.encode("utf-8"))==1):
        #                         idNo=x[j].getAttribute('id')
        #                         no=int(idNo)
        #                         no=no+1
        #                         idNumber=str(no)
        #                         # print(idNumber)
        #                         r=0
        #                         for f in xmlFile.getElementsByTagName("region"):
        #                             y = xmlFile.getElementsByTagName("region")
        #                             Tags=y[r].getAttribute('id') 
        #                             # tages2=Tags.childNodes
        #                             r=r+1
        #                             # print(Tags)
        #                             for tages2 in f.childNodes:
        #                                 if(Tags==idNumber):
        #                                     print(tages2.data.encode("utf-8"))
        #                                     text=tages2.data.encode("utf-8")
        #                                     filtered_sentence1.append(tages2.data.encode("utf-8"))
        #                         for node1 in xmlFile.nodeName:
        #                             # for(i = 0; i < x.length; i=i+1 ){ 
        #                             txt2=x[j].getAttribute('id')
        #                             if(txt2=='6'):
        #                                 print("pawi")         
        #         j=j+1        
            # summarizationProcess(text)
    if(text==""):
        print('Informaation Not Found!!!')
        return "Not found"
    else:
        print('found!!!')      
            # jk=filtered_sentence1
        jk=' '.join(filtered_sentence1)
            # print(jk)           
        return summary(jk)
def getInfo(XmlDocument,r,idNumber,no):
    xmlFile = parse(XmlDocument) 
    for f in xmlFile.getElementsByTagName("region"):
                                    y = xmlFile.getElementsByTagName("region")
                                    Tags=y[r].getAttribute('id') 
                                    r=r+1
                                    for tages2 in f.childNodes:
                                        if(Tags==idNumber):
                                            no=no+1
                                            idNumber=str(no)
                                            print(tages2.data.encode("utf-8"))
                                            text=tages2.data.encode("utf-8")
                                            filtered_sentence1.append(tages2.data.encode("utf-8"))
                                            state="found"
def summarizationProcess(extractedInfo):
    sentence=split_sentences(extractedInfo)
    # print(sentence)
    sentCount=0
    for line in sentence:
        sentCount=sentCount+1
    print("Count : zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",sentCount)    
    if(sentCount>60):
        print 'Input text:'
        print extractedInfo

        print 'Summary:'
        print summarize(extractedInfo, split=True)
        summarizedText=summarize(extractedInfo, split=True)
        return summarizedText
    else:
        print('Summarized information',extractedInfo)
        return extractedInfo
findAnswer(['AI For Undergraduate Students.xml','SRSDocument-Learning tool.xml'],['Semi Supervised Learning' ,'asd'])

