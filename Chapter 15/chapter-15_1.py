from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy

nlp = spacy.load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()
processed_reviews = []
corpus = [
    'The cat sat on the mat.',
    'The dog sat on the log.',
    'Cats and dogs are great pets.',
    'I have a cat; I have a dog.'
]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())