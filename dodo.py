def task_install():
    """install """
    return {
        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* zappala@cs660.byu.edu:/var/www/cs660.byu.edu'],
        }
