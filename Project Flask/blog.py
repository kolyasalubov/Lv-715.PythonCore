from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from init import app, db, manager
from user import User
from article import Article


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/home')
@login_required
def index():
    return render_template("index.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pass = generate_password_hash(password)
            new_user = User(login=login, password=hash_pass)

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

    return render_template('registration_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page)
        else:
            flash('Login or password is not correct. Please check it out and try again')
    else:
        flash('Please fill the login and password fields')

    return render_template('login_page.html')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)

    return response


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/create-article', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        db.session.add(article)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template("create_article.html")


@app.route('/posts/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_article(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "There is something wrong... Please try later"
    else:
        return render_template("update_article.html", article=article)


@app.route('/posts')
@login_required
def get_articles():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("articles.html", articles=articles)


@app.route('/posts/<int:id>')
@login_required
def get_details(id):
    article = Article.query.get(id)
    return render_template("article.html", article=article)


@app.route('/posts/<int:id>/delete')
@login_required
def delete_article(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "There is something wrong... Please try later"


@app.route('/None')
@login_required
def none_redirect():
    return redirect('/')


@app.route('/about')
@login_required
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
