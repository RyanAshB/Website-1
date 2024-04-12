from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/invitational')
def invitational():
    return render_template('invitational.html')

@app.route('/super-league')
def super():
    return render_template('super-league.html')
    

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
