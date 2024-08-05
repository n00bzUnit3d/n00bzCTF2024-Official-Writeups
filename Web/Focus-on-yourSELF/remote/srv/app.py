#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from base64 import b64encode
import os
import hashlib
import subprocess

app = Flask(__name__)

@app.route("/")
def show_gallery():
    # show a gallery of predetermined images
    return render_template("gallery.html")
    
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    # allow to upload an image into /uploads
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Error: No file selected"
        file = request.files['file']
        name = hashlib.sha256(os.urandom(16)).digest().hex()
        file.save(f"/srv/uploads/{name}")
        return redirect(url_for("view_image", image=name))
    return render_template("upload.html")

@app.route("/view")
def view_image():
    # view a specific image
    image = request.args.get('image', '')
    if image == '':
        return "Huh"
    else:
        try:
            with open(f'/srv/uploads/{image}', 'rb') as f:
                return render_template("view.html", url=f"data:image/jpeg;base64, {b64encode(f.read()).decode()}")
        except FileNotFoundError:
                return render_template("view.html", url="https://placehold.co/600x400")

if __name__ == '__main__':
    app.run('0.0.0.0', 1337)
