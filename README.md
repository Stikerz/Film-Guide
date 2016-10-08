1. Install virtualwrapper (http://virtualenvwrapper.readthedocs.io/en/latest/)
2. Create database named `movie_app` still you can use any database name
3. Open config.py file and update the credentials of your database and api connections
4. Run `pip install -r requirements.txt`
5. Run `pip install -r requirements/local.txt`
6. Run `pip install -r requirements/compiled.txt`
7. Run `pip install -r requirements/production.txt`
8. Run `python manage.py migrate allauth`
9. Run `python manage.py migrate base`
10. Run `python manage.py filmlist`			# This can be used as cron to fetch the movies
11. Run `python manage.py runserver`		# Now go to localhost:8000 you will see the films