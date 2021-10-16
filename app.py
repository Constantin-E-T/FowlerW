from flask import Flask, render_template, url_for

from flask_moment import Moment

app = Flask(__name__)

moment = Moment(app)

# dummy posts
posts = [
    # List's
    {
        'author': 'Emilian Constantin',
        'title': 'Blog Post 1',
        'content': 'First post content!',
        'date_posted': 'June 10, 2021'
    },
    {
        'author': 'Diana Andreia',
        'title': 'Blog Post 2',
        'content': 'Second post content!',
        'date_posted': 'June 12, 2021'
    }
]


@app.route('/')
def home():  # ☟ Put the post in HTML page
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run()
