from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('numbers', __name__)


@bp.route('/numbers', methods=('GET', 'POST'))
def numbers():
    if request.method == 'POST':
        numbers = request.form['number_string'].split(";")
        error = None

        if not numbers:
            error = 'Text is required.'

        if error is not None:
            flash(error)
        else:
            asc_numbers = sorted(numbers)
            desc_numbers = sorted(numbers, reverse=True)
            even_numbers = []
            for number in numbers:
                if int(number)%2==0:
                    even_numbers.append(number)
            return render_template('numbers/form.html', asc_numbers=asc_numbers, desc_numbers=desc_numbers, even_numbers=even_numbers)

    return render_template('numbers/form.html')