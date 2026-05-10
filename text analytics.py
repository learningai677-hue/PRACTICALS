# Step 1 - Import Required Libraries

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer


# Step 2 - Download Required NLTK Packages

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


# Step 3 - Create Sample Text Document

text = """
Data Science is an interdisciplinary field that uses
scientific methods, algorithms and systems to extract
knowledge and insights from structured and unstructured data.
"""


# Step 4 - Tokenization

tokens = word_tokenize(text)

print("Tokens")
print(tokens)


# Step 5 - POS Tagging

pos = pos_tag(tokens)

print("\nPOS Tagging")
print(pos)


# Step 6 - Stopwords Removal

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("\nAfter Stopword Removal")
print(filtered_words)


# Step 7 - Stemming

stemmer = PorterStemmer()

stemmed_words = []

for word in filtered_words:
    stemmed_words.append(stemmer.stem(word))

print("\nStemmed Words")
print(stemmed_words)


# Step 8 - Lemmatization

lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in filtered_words:
    lemmatized_words.append(lemmatizer.lemmatize(word))

print("\nLemmatized Words")
print(lemmatized_words)


# Step 9 - TF-IDF Vectorization

documents = [text]

tfidf = TfidfVectorizer()

result = tfidf.fit_transform(documents)

print("\nTF-IDF Values")
print(result.toarray())


# Step 10 - Display Feature Names

print("\nFeature Names")
print(tfidf.get_feature_names_out())