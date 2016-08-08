Speak Agent coding challenge for backend developers
===================================================

Thank you for taking the time to take our backend coder challenge! 

With this challenge, we have some specific skills that we’re looking for:

- The ability to set up your local environment
- The ability to modify existing code
- Knowledge of how to use Git / Github, Python, and Django
- The ability to read documentation for libraries / services you may not be familiar with
- The ability to follow requirements and instructions
- The ability to ask questions when stuck and communicate with colleagues

With that, here are the instructions for this challenge. Please read through them thoroughly and make sure to complete every section. Someone from the Speak Agent team will be available for questions, so please do not hesitate to contact them if you get stuck!

> Please take your time with this challenge. We would much rather wait a week to see a project that works than get a project that doesn’t work after 24 hours.

Note: You should be making regular git commits as you work!

Set up your local environment
-----------------------------

Go to the Github repo and create a fork of the repository. Using virtualenv, install the Django project onto your local machine. Set up the database and add some data.

Make some modifications
-----------------------

The student model under the Student app is fairly barebones. Add the following fields:

- Date of birth
- Grade

Add a view
----------

Create a new view for getting all students in the database of the same grade. Add a new route and a template to display the data from this view. It should look something like this:

***

All students
============

- Abner, Jill - Grade K, born 6/2/2011
- Bela, Juan - Grade 1, born 2/2/201
...

***

Add new models
--------------

In the Student app, add two new models: School and Teacher. The fields for each:

School:
  Title, address

Teacher:
  First name, last name

Hook up the new models to Student
---------------------------------

Each student has one school, but can have multiple teachers. Add these fields to the student model and migrate the database.

Add in Django Rest Framework
----------------------------

Our work at Speak Agent relies heavily on the Django Rest Framework. It’s okay if you’re not familiar with it, but being able to read the documentation and set up a simple call will show us that you can quickly get up to speed with our architecture.

Here is the link to the Django Rest Framework documentation: http://www.django-rest-framework.org/. It may be helpful to also go through the DRF tutorial: http://www.django-rest-framework.org/#tutorial.

Now that the app is set up, create two API calls: 
- One for getting one student by PK
- One for getting all students in the system

The JSON returned from the calls should look something like this:

Single student:

    {
        first_name: first_name,
        last_name: last_name,
        grade: grade,
        dob: date
    }

All students:

    {
        [
            first_name: first_name,
            last_name: last_name,
            grade: grade,
            dob: date
        ],
        ...
    }

***

Make sure that these calls work before moving onto the next section.

Deploy to Heroku
----------------

> Heroku is another important part of our architecture. Once again, it’s okay if you’re not familiar with it, but being able deploy a site to Heroku will show us that you can quickly get up to speed with our architecture. 

> Here is a link to the Heroku documentation about getting a Django site set up on their dynos: https://devcenter.heroku.com/articles/deploying-python

Now that the app is complete, you’ll need to deploy it to Heroku. Note: Please use the free tier! 

Deploy the app to Heroku, create some data, and create an admin login for a member of the Speak Agent team to use.

Submit the app to Speak Agent
-----------------------------

Create a pull request on the Speak Agent repo and email Speak Agent a link to your Heroku site, including the admin username and password that you created. We’ll contact you within a few days!

