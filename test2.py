from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent1 =["qwe","asd","ewq","aqw"] 
example_sent2 = "qwe"

def sim(keywords, heading):
    for k in keywords:
        stop_words = set(stopwords.words('english'))
        result = ''.join([i for i in heading if not i.isdigit()])
        word_tokens1 = word_tokenize(k.lower())
        word_tokens2 = word_tokenize(result.lower())

        # filtered_sentence1 = [w for w in word_tokens1 if not w in stop_words]
        # filtered_sentence2 = [w for w in word_tokens2 if not w in stop_words]
        filtered_sentence1 = []
        filtered_sentence2 = []

        for w in word_tokens1:
            if w not in stop_words:
                filtered_sentence1.append(w)
        for w in word_tokens2:
            if w not in stop_words:
                filtered_sentence2.append(w)
        # print(word_tokens1)
        # print(filtered_sentence1)
        # print(word_tokens2)
        # print(filtered_sentence2)

        ratio = float(len(set(filtered_sentence1).intersection(filtered_sentence2))) / float(len(set(filtered_sentence1).union(filtered_sentence2)))
        # print("ratio: ",ratio)
        if(ratio>0.55):
            return 1 


    return 0      

print(sim(['satisfication document','asd'],'Document the satisfication'))    