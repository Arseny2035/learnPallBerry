from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str):
    with open('vsearch.log', 'a') as logfile:
        print(req, res, file=logfile)


@app.route('/search4', methods=['POST'])
def search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results!'
    results = str((search4letters(phrase, letters)))
    log_request(request, results)
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

@app.route('/viewlog', methods=['POST'])
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)

if __name__ == '__main__':
    app.run(debug=True)
