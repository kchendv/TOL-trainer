import os
import sys
import secrets
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/answer_files', picture_fn)
    i = Image.open(form_picture)
    i.save(picture_path)
    print(picture_path)
    return picture_fn


def save_pdf(form_pdf):
    random_hex = secrets.token_hex(8)
    file_fn = random_hex + '.pdf'
    file_path = os.path.join(current_app.root_path, 'static/answer_files', file_fn)
    form_pdf.save(file_path)
    return file_fn
