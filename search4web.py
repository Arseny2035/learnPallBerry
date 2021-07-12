from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results!'
    results = str((search4letters(phrase, letters)))

    return render_template('result.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on thw web!')


app.run(debug=True)
