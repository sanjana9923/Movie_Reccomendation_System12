from flask import Flask, Response, request, render_template
from main import recommendation

app = Flask(__name__)

@app.route("/movierecommedation", methods = ["GET", "POST"])
def recommend():
    if request.method == "POST":
        movie = request.form["favorite_movie_name"]
        recommended_movie = recommendation(movie)
        return render_template("result.html", movie=recommended_movie)
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)


