import numpy as np # linear algebra
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("udemy_courses.csv")

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["course_title"], df["subject"])
# feature_names = vectorizer.get_feature_names()
# dense = vectors.todense()
# denselist = dense.tolist()
# df = pd.DataFrame(denselist, columns=feature_names)

query = "Python"
query_vec = vectorizer.transform([query])

results = cosine_similarity(vectors,query_vec)
resultsIndexes = results.argsort()
for index in resultsIndexes[-10:]:
    print(index)