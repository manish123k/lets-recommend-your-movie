import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie, new, similarity):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    name = []
    poster = []
    for i in distances[0:30]:
        poster.append(fetch_poster(new.iloc[i[0]].movie_id))
        name.append(new.iloc[i[0]].title)
    return name, poster


def main():
    pickle_file = open("movie_dict.pkl", "rb")
    df = pickle.load(pickle_file)
    movies = pd.DataFrame(df)
    # st.header("movies_hub")
    st.title("welcome to movie recommender system")
    option = st.selectbox("which movie would you like?", movies["title"])

    pickle_file = open("similarity.pkl", "rb")
    model = pickle.load(pickle_file)

    if st.button('Recommend'):
        name, poster = recommend(option, movies, model)
        j = 0
        # row 1
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1
        # row 2
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1
        #row 3
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1

        #row 4
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1
        # row 5
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1
        #row 6
        for i in st.columns(5):
            with i:
                st.text(name[j])
                st.image(poster[j])
            j += 1

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
