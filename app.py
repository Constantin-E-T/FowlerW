from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_moment import Moment

app = Flask(__name__)
# Create a secret key ❖ to create one very easy go to python console log and
# >>> import secrets
# >>> secrets.token_hex(ex:16)
app.config['SECRET_KEY'] = '1acff3c0d6ebf1dd037206a55d48024a'

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
def home():
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():  # ☟ Put the post in HTML page
    return render_template('blog.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Make a form instance
    form = RegistrationForm()

    # Create a validation for submit form with user name and if validate ok,
    # send the user to home page with a success message
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    # Pass title and the form instance                              ⤵︎
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Make a form instance from forms.py
    form = LoginForm()

    # Create a validation for submit form with user name and if validate ok,
    # send the user to home page with a success message
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password' and form.username.data == 'Con':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    # Pass title and the form instance                              ⤵︎
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
