from flask import Flask, render_template
import requests


app = Flask(__name__)
url = 'https://api.npoint.io/c790b4d5cab58020d391'
posts = requests.get(url).json()
print(posts)

@app.route('/')
def home():
    length = len(posts)
    return render_template("index.html", posts=posts, len=length)
@app.route('/<int:num>')
def blog(num):
    return  render_template('post.html', num=num-1, posts=posts)
if __name__ == "__main__":
    app.run(debug=True)