from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('mimificator', __name__)


@bp.route('/mimificator', methods=('GET', 'POST'))
def mimificator():
    vowels = "aAÁeéÉoOÓ"
    if request.method == 'POST':
        phrase = request.form['phrase']

        error = None

        if not phrase:
            error = 'Text is required.'

        if error is not None:
            flash(error)
        else:
            mimi_phrase = phrase
            for vowel in vowels:
                mimi_phrase = mimi_phrase.replace(vowel, "i")

            return render_template('mimificator/form.html', phrase=mimi_phrase)

    return render_template('mimificator/form.html')