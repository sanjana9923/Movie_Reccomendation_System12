import pandas as pd
import numpy as np
import difflib
import pickle

Similarity_Score = pickle.load(open("ssScore.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))
def recommendation(Movie_Name):
    recommended_movie = []
    list_of_all_titles = df['Movie_Title'].tolist()
    Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)
    Close_Match = Find_Close_Match[0]
    Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
    Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))
    sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
    print('Top 10 movies suggested for you:\n')
    i=1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = df[df.Movie_ID == index]['Movie_Title'].values
        if(i<11):
            recommended_movie.append([i,'.',title_from_index])
            i+=1
    return recommended_movie
    