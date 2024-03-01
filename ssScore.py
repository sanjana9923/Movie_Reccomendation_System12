import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')
df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')
x = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' '+df_features['Movie_Cast']+' '+ df_features['Movie_Director']
tfidf = TfidfVectorizer()
x = tfidf.fit_transform(x)
Similarity_Score = cosine_similarity(x)
pickle.dump(Similarity_Score, open("ssScore.pkl", "wb"))
pickle.dump(df, open("df.pkl", "wb"))