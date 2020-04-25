from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('dates', __name__)


@bp.route('/dates', methods=('GET', 'POST'))
def dates():
    format = "%Y-%m-%d"
    if request.method == 'POST':
        first_date = request.form['first_date']
        second_date = request.form['second_date']

        error = None

        if not first_date or not second_date:
            error = 'Text is required.'
        else:
            first_date = datetime.strptime(first_date, format)
            second_date = datetime.strptime(second_date, format)

        if error is not None:
            flash(error)
        else:
            days = abs((first_date-second_date).days)
            weekday = days // 7
            month = days // 30
            return render_template('dates/form.html', days=days, weekday=weekday, month=month)

    return render_template('dates/form.html')