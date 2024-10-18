# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:28:40 2024

@author: Arnav Jain
"""

import streamlit as st
import pickle
import pandas as pd
import difflib


def recommend(movie_name):
    movie_list=movies['title'].tolist()
    find_close_match=difflib.get_close_matches(movie_name,movie_list)
    close_match=find_close_match[0]

    index= movies[movies.title==close_match]['index'].values[0]
    
    similarity_score=list(enumerate(similarity[index]))
    sorted_similarity_score=sorted(similarity_score, key = lambda x:x[1] ,reverse=True)[1:6]

    
    recomm_movies=[]
    for i in sorted_similarity_score:
        recomm_movies.append(movies.iloc[i[0]].title)
    return recomm_movies


similarity=pickle.load(open("C:/Users/Arnav Jain/Desktop/New folder/similarity.pkl",'rb'))            
movies_list=pickle.load(open("C:/Users/Arnav Jain/Desktop/New folder/movies_data.pkl",'rb'))
movies=pd.DataFrame(movies_list)

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'Select a movie',movies['title'].values
    )


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i) 
    