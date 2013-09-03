import sys

from views import fall2013

from flask import Flask, render_template
from flask_frozen import Freezer

from config import app, freezer

@app.route('/',defaults={'directory':None,'page':'index'})
@app.route('/<page>',defaults={'directory':None})
@app.route('/<path:directory>/',defaults={'page':'index'})
@app.route('/<path:directory>/<page>')
def show(directory,page):
    try:
        if not directory:
            return render_template(page + '.html')
        return render_template(directory+"/" + page + '.html')
    except:
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
