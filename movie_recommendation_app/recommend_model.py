import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

df = pd.read_csv("movies.csv")

df['genres'] = df['genres'].apply(lambda x: x.split('|')).apply(lambda x: ' '.join(x))

title = df['title'].apply(lambda x: re.sub(r'\(\d+\)', '', x).strip())

df['title'] = title

df['text'] = df['genres'] + ' ' + df['title']

df['text'] = df['text'].apply(lambda x: x.lower())

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(df['text']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(df.iloc[i[0]]['title'])

    return recommended_movies

