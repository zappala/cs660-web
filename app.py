import os
import sys

from views import winter2017
from views import fall2014
from views import fall2013

from flask import Flask, render_template
from flaskext.markdown import Markdown
from flask_frozen import Freezer

from config import app, freezer

Markdown(app)

@app.route('/',defaults={'directory':None,'page':'index'})
@app.route('/<page>',defaults={'directory':None})
@app.route('/<path:directory>/',defaults={'page':'index'})
@app.route('/<path:directory>/<page>')
def show(directory,page):
    if not directory:
        filename = page + '.html'
        if os.path.isfile('templates/' + filename):
            return render_template(filename, active='home')
        print filename
        return render_template('404.html'), 404
    try:
        prev = directory.split('/')[-1]
    except:
        prev = None
    filename = directory + "/" + page + '.html'
    if os.path.isfile('templates/' + filename):
        return render_template(filename, active=page, previous=prev)
    print filename
    return render_template('404.html'), 404

@freezer.register_generator
def custom404():
    yield '/404'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)
