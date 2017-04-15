# Installation #

1. Create a folder and go to it:

        mkdir project
        cd project

2. Clone project from GitHub:

        git clone https://github.com/andsimakov/bizzfuzz

3. Create a virtual environment in folder 'venv' for the app and activate it:

        python3 -m venv venv
        . venv/bin/activate

4. Install requirements using pip:

        pip install -r bizzfuzz/requirements.txt

5. Run a migration:

        cd bizzfuzz
        ./manage.py makemigrations bizzfuzz
        ./manage.py migrate --fake-initial

6. Run the app:

        ./manage.py runserver

7. Open your browser and access the app:

        localhost

The empty List View should appear. Now the app is ready for work.

- - - -

# Release Notes #

1. The app has been developed for Python3.6/Django 1.11 with and RDBMS SQLite as a datasource.
2. The app's UI is based on Materialize CSS/JS library.
3. Default User model has been extended with 'birthday' and 'random' fields by Profile model via OneToOneField relation.
4. Implemented views: Profile List, Profile details, Create Profile, Edit Profile and Delete Profile.
5. Profile List view has been enriched with all profile attributes.
6. Extra template tags added: 
    * __'status'__: displays "allowed" for a user above 13 y.o. otherwise "blocked".
    * __'bizzfuzz'__: displays BizzFuzz result based on random number generated for a user according to the spec: for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz". Otherwise displays random number itself.
7. Exporting Entire Profile List to CSV-file extra feature has been implemented.

# ToDo #

Add unit tests.