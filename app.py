from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_movie = request.form['movie']
        index = movies[movies['title'] == selected_movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movies = []
        for i in distance[1:6]:
            recommend_movies.append(movies.iloc[i[0]].title)
        return render_template('index.html', movies_list=movies_list, selected_movie=selected_movie, recommend_movies=recommend_movies)
    return render_template('index.html', movies_list=movies_list)

if __name__ == '__main__':
    app.run(debug=True)