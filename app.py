import streamlit as st
import pickle
import pandas as pd
import requests
# import streamlit.components.v1 as com
# import flask
# from flask import Flask,render_template

# app = Flask(__name__)
#
# @app.route('/')
# def index():
#  return (render_template('test-1.html'))
#
# if __name__ == '__main__':
#     app.run(debug=True)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e29cc4a249b1a6728841bb380b5bbf23&language=en-US'.format(movie_id))
    data = response.json()
    print (data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
   index = movie_list[movie_list['title'] == movie].index[0]
   distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
   recommended_movie_posters = []
   recommended_movies = []
   for i in distances[0:21]:
    movie_id = movie_list.iloc[i[0]].movie_id
    recommended_movies.append(movie_list.iloc[i[0]].title)
    recommended_movie_posters.append(fetch_poster(movie_id))
   return recommended_movies,recommended_movie_posters

movie_list = pickle.load(open('movie_list.pkl', 'rb'))
movie_list = pd.DataFrame(movie_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Trending movies')
st.image('https://th.bing.com/th/id/OIP.MnIKm9v_ZKjwT7681T76SQHaD5?pid=ImgDet&rs=1')
selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movie_list['title'].values

)

if st.button('Enter'):
    recommended_movies, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5,  = st.columns(5)

    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movie_posters[3])
    with col5:
            st.text(recommended_movies[4])
            st.image(recommended_movie_posters[4])

    with col1:
        st.text(recommended_movies[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movies[6])
        st.image(recommended_movie_posters[6])

    with col3:
        st.text(recommended_movies[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movies[8])
        st.image(recommended_movie_posters[8])
    with col5:
            st.text(recommended_movies[9])
            st.image(recommended_movie_posters[9])
    with col1:
        st.text(recommended_movies[10])
        st.image(recommended_movie_posters[10])
    with col2:
        st.text(recommended_movies[11])
        st.image(recommended_movie_posters[11])

    with col3:
        st.text(recommended_movies[12])
        st.image(recommended_movie_posters[12])
    with col4:
        st.text(recommended_movies[13])
        st.image(recommended_movie_posters[13])
    with col5:
        st.text(recommended_movies[14])
        st.image(recommended_movie_posters[14])
    with col1:
        st.text(recommended_movies[15])
        st.image(recommended_movie_posters[15])
    with col2:
        st.text(recommended_movies[16])
        st.image(recommended_movie_posters[16])

    with col3:
        st.text(recommended_movies[17])
        st.image(recommended_movie_posters[17])
    with col4:
        st.text(recommended_movies[18])
        st.image(recommended_movie_posters[18])
    with col5:
        st.text(recommended_movies[19])
        st.image(recommended_movie_posters[19])


