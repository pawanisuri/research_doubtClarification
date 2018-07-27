# Imports
from string import punctuation
from colorama.initialise import init
from _collections import defaultdict
import nltk
# import nltk.corpus
from nltk.corpus import stopwords
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
# Get default English stopwords and extend with punctuation
# stopwords = nltk.corpus.stopwords.words('english')
# stopwords.extend(string.punctuation)
# stopwords.append('')

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

# Create tokenizer and stemmer
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
stemmer = nltk.stem.snowball.SnowballStemmer('english')
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def is_ci_token_stopword_set_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(b)))
    print(pos_a)
    print(pos_b)
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    # stopWords = set(stopwords.words('english'))
    # stopWords = set(stopwords.words('english'))
    # lemmae_a = word_tokenize(a)
    # lemmae_b = word_tokenize(b)
    
        
    print(lemmae_a)
    print(lemmae_b)
    print(float(len(set(lemmae_a).intersection(lemmae_b))))
    print(float(len(set(lemmae_a).union(lemmae_b))))
    # Calculate Jaccard similarity
    ratio = float(len(set(lemmae_a).intersection(lemmae_b))) / float(len(set(lemmae_a).union(lemmae_b)))
    print(ratio)
    return (ratio >= threshold)

print(is_ci_token_stopword_set_match("I am Pawani suriyaarachchi","My Name is Pawani suriyaarachchi",0.5))