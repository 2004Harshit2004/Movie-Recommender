
import streamlit as st

import pickle
new_movies=pickle.load(open('models/movies.pkl','rb'))
movie_list=new_movies['title'].values

similairity=pickle.load(open('models/similarity.pkl','rb'))

def recommend(movie):
    lists=[]
    index=new_movies[new_movies['title']==movie].index[0]
    simi=similairity[index]
    simil=list(enumerate(simi))
    arr=sorted(simil,reverse=True,key=lambda x:x[1])

    count=0
    for i in range(len(arr)):
        if(count<6):
            name=new_movies['title'][arr[i][0]]
            lists.append(name)
            count+=1
        else :
            break
    return lists

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Enter movie name",
    movie_list,
    # ("Email", "Home phone", "Mobile phone"),
)

# st.button("Recommend", type="primary")
if st.button("Recommend"):
    recommended=recommend(selected_movie_name)
    for i in recommended:
        st.write(i)



