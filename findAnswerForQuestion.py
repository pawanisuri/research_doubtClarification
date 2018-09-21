import xml.etree.ElementTree as ET
import re
from xml.dom.minidom import parse, Node
from test2 import sim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization.textcleaner import split_sentences
from gensim.summarization import summarize

# from stringMatching import is_ci_token_stopword_set_match
# xmlFile = parse("SRSDocument-Learning tool.xml")

def findAnswer(XmlDocumentset,startPage,endPage,keywords):
    extractedSentences=[None]*10000
    txt = ""
    status="notFound"
    filtered_sentence1 = []
    text=""
    # tree = ET.parse(xmlFile)
    h="DoCO:SectionTitle"
    
    for XmlDocument in XmlDocumentset:     
        xmlFile = parse(XmlDocument)   
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
    if(text==""):
        print('Informaation Not Found!!!')
    else:
        print('found!!!')      
            # jk=filtered_sentence1
        jk=' '.join(filtered_sentence1)
            # print(jk) 
        summarizationProcess(jk)  
# text ="Thomas A. Anderson is a man living two lives. By day he is an " + \
#     "average computer programmer and by night a hacker known as " + \
#     "Neo. Neo has always questioned his reality, but the truth is " + \
#     "far beyond his imagination. Neo finds himself targeted by the " + \
#     "police when he is contacted by Morpheus, a legendary computer " + \
#     "hacker branded a terrorist by the government. Morpheus awakens " + \
#     "Neo to the real world, a ravaged wasteland where most of " + \
#     "humanity have been captured by a race of machines that live " + \
#     "off of the humans' body heat and electrochemical energy and " + \
#     "who imprison their minds within an artificial reality known as " + \
#     "the Matrix. As a rebel against the machines, Neo must return to " + \
#     "the Matrix and confront the agents: super-powerful computer " + \
#     "programs devoted to snuffing out Neo and the entire human " + \
#     "rebellion. "+\
#     "Thomas A. Anderson is a man living two lives. By day he is an " + \
#     "average computer programmer and by night a hacker known as " + \
#     "Neo. Neo has always questioned his reality, but the truth is " + \
#     "far beyond his imagination. Neo finds himself targeted by the " + \
#     "police when he is contacted by Morpheus, a legendary computer " + \
#     "hacker branded a terrorist by the government. Morpheus awakens " + \
#     "Neo to the real world, a ravaged wasteland where most of " + \
#     "humanity have been captured by a race of machines that live " + \
#     "off of the humans' body heat and electrochemical energy and " + \
#     "who imprison their minds within an artificial reality known as " + \
#     "the Matrix. As a rebel against the machines, Neo must return to " + \
#     "the Matrix and confront the agents: super-powerful computer " + \
#     "programs devoted to snuffing out Neo and the entire human " + \
#     "rebellion. "

def summarizationProcess(extractedInfo):
    sentence=split_sentences(extractedInfo)
    # print(sentence)
    sentCount=0
    for line in sentence:
        sentCount=sentCount+1
    print("Count : zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",sentCount)    
    if(sentCount>10):
        print 'Input text:'
        print extractedInfo

        print 'Summary:'
        print summarize(extractedInfo, split=True)
        summarizedText=summarize(extractedInfo, split=True)
        return summarizedText
    else:
        return extractedInfo
findAnswer(['Data Communication Networking.xml','android_tutorial.xml'],2,3,["Summary","Ring Topology","5. ANDROID Hello World Example Android", "If not, there is a tangible financial risk to core business operations."])

