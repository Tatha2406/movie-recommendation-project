import streamlit as st
import pandas as pd
import requests
import pickle

def fetch_poster(movie_id, api_key):
    base_url = 'https://api.themoviedb.org/3/movie/'
    api_url = f'{base_url}{movie_id}?api_key={api_key}'
    
    try:
        # Send a GET request to the TMDb API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        data = response.json()
        
        # Check if 'poster_path' is present in the response data
        if 'poster_path' in data:
            poster_path = data['poster_path']
            poster_url = f'https://www.themoviedb.org/t/p/w500/{poster_path}'
            return poster_url
        else:
            return "Poster not found for this movie."
    except requests.exceptions.RequestException as e:
        return f"Error fetching movie data: {e}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(movie_distance)), reverse=True, key=lambda x: x[1])[1:7]

    recommend_movies = []
    recommend_movies_poster= []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id,api_key)) 
    return recommend_movies,recommend_movies_poster

all_movie = pickle.load(open('all_movie.pkl','rb'))
movies=pd.DataFrame(all_movie)
api_key = '6c5ca09a90449fa112274a2d9533da41' 

st.title("Movie Recommender System")

similarity = pickle.load(open('similarity.pkl','rb'))

option = st.selectbox(
    'Enter movie name?',
        movies['title'].values) 
if st.button('Recommend'):

    names,posters = recommend(option)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
   



 




 

