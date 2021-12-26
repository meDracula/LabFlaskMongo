from flask import Blueprint, render_template

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    from app.controller.user_controller import get_all_users
    users = get_all_users()
    return render_template('index.html', users=users)


@bp_open.get('/about')
def about():
    return render_template('about.html')


@bp_open.get('/labratory')
def labratory():
    from app.controller.researchers_controller import get_all_researchers
    researcher = get_all_researchers()
    print(researcher)
    return render_template('labratory.html', researcher=researcher)

