Fork based on Speak Agent coding challenge for backend developers
============

### Description

- Created local virtual environment using `virtualenv` command.

- Added fields date_of_birth and grade to Student model.

- Created urls.py for student app and created two types of views, Class Based View and a simple Function Based View (this code lines are commented), these views filter all students with grade = 'K'.

- Created base.html template and student_list.html template to show a list of the students from the database.

- Added new model named School with fields title and address.

- Added new model named Teacher with fields first_name and last_name.

- Hookup models to Student model, each student has one school, but can have multiple teachers.

- Added Django Rest Framework and created two api calls, one to retrieve a [list of all students](https://speakagentchallenge.herokuapp.com/api/students/) and one to [retrieve students by PK](https://speakagentchallenge.herokuapp.com/api/students/1/).

- Deployed application to Heroku, application URL: [https://speakagentchallenge.herokuapp.com](https://speakagentchallenge.herokuapp.com).  Created some data for the deployed application.

### Installation Steps


Clone this repository and open the Terminal on the root folder of the project.  And run this commands:

~~~~
virtualenv venv
source venv/bin/activate
pip install -r requirements/dev.txt
./studentsite/manage.py migrate
./studentsite/manage.py createsuperuser
./studentsite/manage.py runserver
~~~~
