import nltk
# # Imports
from string import punctuation
# # from colorama.initialise import init 
from _collections import defaultdict
# import nltk
# # import nltk.corpus
from nltk.corpus import stopwords
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
import re, math
from collections import Counter
from sklearn.metrics import jaccard_similarity_score
# # Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')
# # Create tokenizer and stemmer
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
stemmer = nltk.stem.snowball.SnowballStemmer('english')
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

def get_most_matching_topic(rationList):
    max=rationList[0]
    for count in range(0,len(rationList)):
        if max<rationList[count]:
            max=rationList(count)
    return max            

def is_ci_token_stopword_set_match(a, b, threshold=0.5):
     """Check if a and b are matches."""
     stopwords = nltk.corpus.stopwords.words('english')
     stopwords.extend(string.punctuation)
     stopwords.append('')
     print(stopwords)
     # # Create tokenizer and stemmer
     tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
     stemmer = nltk.stem.snowball.SnowballStemmer('english')
     lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

     i=0
     allRations=[None]*100
    #  print("length",len(b))
     for  x in range(i,len(b)):
        pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
        pos_b = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(b[x])))
        # print(pos_a)
        # print(pos_b)
        lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                        if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
        lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                        if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
        # stopWords = set(stopwords.words('english'))
        filtered_sentence = []
         # stopWords = set(stopwords.words('english'))
        lemmae_a = word_tokenize(pos_a)
        # lemmae_b = word_tokenize(b[i])
        for w in lemmae_a:
            print(w)
            if w not in stopwords:
                filtered_sentence.append(w)
        print(filtered_sentence)        
            
        # print(lemmae_a)
        # print(lemmae_b)
        # print(float(len(set(lemmae_a).intersection(lemmae_b))))
        # print(float(len(set(lemmae_a).union(lemmae_b))))
         # Calculate Jaccard similarity
        # print("i value", i)
        # print(len(allRations))
        ratio = float(len(set(lemmae_a).intersection(lemmae_b))) / float(len(set(lemmae_a).union(lemmae_b)))
        # if ratio >= threshold:
        #     allRations[i]=ratio
        # ratio=jaccard_similarity_score(lemmae_a, lemmae_b)
        print("ration", ratio)
         # print(b[x])
        i=i+1
     maximum_ratio=get_most_matching_topic(allRations)
     print("max",maximum_ratio)
     return (ratio >= threshold)     
     # return 0

print(is_ci_token_stopword_set_match("satisfication document",["document satisfication","document"],0.1))