from flask import Flask, render_template
from utils import *


app = Flask(__name__)


@app.route('/')
def index_page():
    data = get_all()
    return render_template('index.html', data=data)


@app.route('/candidates/<int:pk>')
def candidates_page(pk):
    data = get_by_pk(pk)
    return render_template('candidates.html', name=data['name'], position=data['position'], skills=data['skills'],
                           img=data['picture'])


@app.route('/skills/<skill_name>')
def candidates_by_skill_page(skill_name):
    data = get_by_skill(skill_name)
    return render_template('skills_page.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
