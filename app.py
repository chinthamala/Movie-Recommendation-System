import streamlit as st
import pickle
import pandas as pd

# Load the movies DataFrame and similarity matrix
movies_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Ensure movies_df is a DataFrame and keep the titles as options
movies_list = movies_df['title'].values


def recommend(movie, movies_df, similarity):
    # Get the index of the selected movie
    movie_index = movies_df[movies_df['title'] == movie].index[0]

    # Retrieve similarity scores for the selected movie
    distances = similarity[movie_index]

    # Sort movies based on similarity score and exclude the first result (itself)
    recommended_indices = sorted(range(len(distances)), key=lambda i: distances[i], reverse=True)[1:6]

    # Collect recommended movie titles
    recommended_movies = []
    for i in recommended_indices:
        recommended_movies.append(movies_df.iloc[i].title)
        #fetch poster from API
        

    return recommended_movies


# Streamlit app setup
st.title('MOVIE RECOMMENDATION SYSTEM')
selected_movie_name = st.selectbox(
    'Choose a movie you like:',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name, movies_df, similarity)
    for i in recommendations:
        st.write(i)
