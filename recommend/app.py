
import streamlit  as st
import pickle
import pandas as pd
import numpy as np
import requests

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values

st.title('Movie Recommendor System')
select_values=st.selectbox("Select movie from dropdown",movies_list)



def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])

    recommended_movie=[]
    # recommend_poster=[]

    for i in distance[1:6]:
        # movies_id=movies.iloc[i[0].id]
        recommended_movie.append(movies.iloc[i[0]].title)
        # recommend_poster
    return recommended_movie


if st.button("show Recommend"):
    movie_name=recommend(select_values)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        # st.image(posters[0])
    with col2:
        st.text(movie_name[1])
        # st.image(posters[1])

    with col3:
        st.text(movie_name[2])
        # st.image(posters[2])
    with col4:
        st.text(movie_name[3])
        # st.image(posters[3])
    with col5:
        st.text(movie_name[4])
        # st.image(posters[4])


























# import streamlit  as st
# import pickle
# import pandas as pd
# import numpy as np
# import requests

# movies=pickle.load(open('movies.pkl','rb'))
# similarity=pickle.load(open('similarity.pkl','rb'))
# movies_list=movies['title'].values

# st.title('Movie Recommendor System')
# select_values=st.selectbox("Select movie from dropdown",movies_list)

# def fetch_poster(movie_id):
#      url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
#      data=requests.get(url)
#      data=data.json()
#      poster_path = data['poster_path']
#      full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
#      return full_path

# def recommend(movie):
#     index=movies[movies['title']==movie].index[0]
#     distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])

#     recommended_movie=[]
#     recommend_poster=[]

#     for i in distance[1:6]:
#         movies_id=movies.iloc[i[0].id]
#         recommended_movie.append(movies.iloc[i[0]].title)
#         recommend_poster.append(fetch_poster(movies_id))
#     return recommended_movie,recommend_poster


# if st.button("show Recommend"):
#     movie_name,posters=recommend(select_values)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(movie_name[0])
#         st.image(posters[0])
#     with col2:
#         st.text(movie_name[1])
#         st.image(posters[1])

#     with col3:
#         st.text(movie_name[2])
#         st.image(posters[2])
#     with col4:
#         st.text(movie_name[3])
#         st.image(posters[3])
#     with col5:
#         st.text(movie_name[4])
#         st.image(posters[4])






