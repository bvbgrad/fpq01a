from flask import (
    Blueprint, render_template
)

from fpq_app.auth import login_required

bp = Blueprint('quiz', __name__)


@bp.route('/', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('quiz/index.html')


@bp.route('/scores', methods=['POST', 'GET'])
@login_required
def display_scores():
    return render_template('quiz/scores.html')
