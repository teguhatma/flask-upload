
from flask import url_for, render_template, request, flash, redirect
from app import app, db
from .forms import UploadForm
from app.models import User
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

@app.route('/', methods=['POST', 'GET'])
def upload():
    form = UploadForm()

    filenames = []
    if request.method == 'POST':
        file_obj = request.files.getlist('file')
        for f in file_obj:

            photos.save(f, name=f.filename)
            
            filenames.append(f.filename)

        user = User(
            username = form.username.data,
            first_name = form.firstName.data,
            last_name = form.lastName.data,
            email = form.email.data,
            photos_filename = filenames,
        )

        db.session.add(user)
        db.session.commit()
        flash("Success")
        return redirect(url_for('upload'))
    return render_template('upload.html', title='Upload a some photos', form=form)