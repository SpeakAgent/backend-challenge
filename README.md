Fork based on Speak Agent coding challenge for backend developers
============
---

## Description

- Created local virtual environment using `virtualenv` command.

- Added fields date_of_birth and grade to Student model.

- Created urls.py for student app and created two types of views, Class Based View and a simple Function Based View (this code lines are commented).

- Created base.html template and student_list.html template to show a list of the students from the database.

- Added new model named School with fields title and address.

- Added new model named Teacher with fields first_name and last_name.

- Added Django Rest Framework and created two api calls, one to retrieve a [list of all students](https://speakagentchallenge.herokuapp.com/api/students/) and one to [retrieve students by PK](https://speakagentchallenge.herokuapp.com/api/students/1/).

- Deployed application to Heroku , application URL: [https://speakagentchallenge.herokuapp.com](https://speakagentchallenge.herokuapp.com).
