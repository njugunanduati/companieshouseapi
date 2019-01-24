from flask import Flask, render_template, request
from app.index import Index

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    template_name = 'index.html'
    return render_template(template_name)


@app.route('/search/', methods=['POST'])
def search():
    word = request.args.get('company_name')
    result = Index.check_comapny_name(word)
    return result


if __name__ == "__main__":
    app.run()
