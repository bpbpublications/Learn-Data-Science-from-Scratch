# import the necessary libraries
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel
import spacy
	
# load the spacy model
nlp = spacy.load('en_core_web_sm')
	
# suppose 'documents' is a list of text documents
documents = ["The quick brown fox jumps over the lazy dog",
             "John bought a new car",
             "The new car is beautiful",
             "Python is a great programming language"]

# perform basic preprocessing (lowercase, tokenization, stopword removal)
texts = [[token for token in doc.lower().split() if token not in gensim.parsing.preprocessing.STOPWORDS] for doc in documents]
	
# create a dictionary representation of the documents
dictionary = corpora.Dictionary(texts)

# convert the list of texts to a list of vectors
corpus = [dictionary.doc2bow(text) for text in texts]

# perform topic modelling using LDA
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=2)
	
# print the topics
topics = lda_model.print_topics(num_words=4)
for topic in topics:
    print(topic)
	
# perform named entity recognition using spacy
for doc in documents:
    spacy_doc = nlp(doc)
    for ent in spacy_doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
