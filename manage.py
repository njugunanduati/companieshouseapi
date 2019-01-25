import json
from flask import Flask, render_template, request
from app.index import Index

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    template_name = 'index.html'
    return render_template(template_name)


@app.route('/search/', methods=['POST'])
def search():
    word = request.form['company_name']
    try:
        result = Index.check_comapny_name(word)
        data = {"status": "Success", "message": result}
    except Exception as e:
        data = {"status": "Error!", "message": str(e)}
    return json.dumps(data)


if __name__ == "__main__":
    app.run()
