# Installation

1. Create a folder and go to it.
1. Clone project from GitHub: https://github.com/andsimakov/bizzfuzz
3. Create a virtual environment for the app.
4. Install requirements using pip:

        pip install -r requirements.txt

5. Run migration

        ./manage.py migrate

# Release Notes

1. The app works has been developed for Python3.6/Django 1.11 with and RDBMS SQLite as a datasource.
2. The app's UI is based on Materialize CSS/JS library.
3. Default User model has been extended with 'birthday' and 'random' fields with Profile model via OneToOneField relation.
4. Implemented views: Profile list, Profile details, Create Profile, Edit Profile and Delete a profile.
5. Profile List view has been enriched with all profile attributes.
6. Extra template tags added: 
    • 'status': displays "allowed" for a user above 13 y.o. otherwise "blocked".
    • 'bizzfuzz': displays BizzFuzz result based on random number generated for a user according to the spec: for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz". Otherwise displays random number itself.
7. Exporting Entire Profile List to CSV-file extra feature has been implemented.


#ToDo

Add unit tests.