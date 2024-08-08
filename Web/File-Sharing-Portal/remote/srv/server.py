#!/usr/bin/env python3
from flask import Flask, request, redirect, render_template, render_template_string
import tarfile
from hashlib import sha256
import os
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    global username
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        file = request.files['file']
        if file.filename[-4:] != '.tar':
            return render_template_string("<p> We only support tar files as of right now!</p>")
        name = sha256(os.urandom(16)).digest().hex()
        os.makedirs(f"./uploads/{name}", exist_ok=True)
        file.save(f"./uploads/{name}/{name}.tar")
        try:
            tar_file = tarfile.TarFile(f'./uploads/{name}/{name}.tar')
            tar_file.extractall(path=f'./uploads/{name}/')
            return render_template_string(f"<p>Tar file extracted! View <a href='/view/{name}'>here</a>")
        except:
            return render_template_string("<p>Failed to extract file!</p>")

@app.route('/view/<name>')
def view(name):
    if not all([i in "abcdef1234567890" for i in name]):
        return render_template_string("<p>Error!</p>")
        #print(os.popen(f'ls ./uploads/{name}').read())
            #print(name)
    files = os.listdir(f"./uploads/{name}")
    out = '<h1>Files</h1><br>'
    files.remove(f'{name}.tar')  # Remove the tar file from the list
    for i in files:
        out += f'<a href="/read/{name}/{i}">{i}</a>'
       # except:
    return render_template_string(out)

@app.route('/read/<name>/<file>')
def read(name,file):
    if (not all([i in "abcdef1234567890" for i in name])):
        return render_template_string("<p>Error!</p>")
    if ((".." in name) or (".." in file)) or (("/" in file) or "/" in name):
        return render_template_string("<p>Error!</p>")
    f = open(f'./uploads/{name}/{file}')
    data = f.read()
    f.close()
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
