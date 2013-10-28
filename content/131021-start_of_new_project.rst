Start of New Project
####################

:date: 2013-10-21 23:59

Today I would like to start a new project. It has the simple aim of me producing code
daily and trying to push it live. The code doesn't have to be productive, it can even be
an experiment, but the aim is purely of getting in to the habit of working daily on 
something, in the hopes of learning. The focus initially will be in the Python_ language. So for the 
first day, the aim is to make an app for tracking these challenges.

:icon:`question-sign` Target
----------------------------

Todays target is to produce an app that:

- Allows you to make a list of challenges.
- Each challenge has a title, difficulty level and description
- Hints can be attached to each challenge which are hidden by default.
- Bonus challenges can be appended to further enhance the challenge.

:icon:`tasks` Result
--------------------

**TL;DR** No progress, side tracked by trying to automate project setup.

So in the end, I didn't even get a chance to start on this. The day was actually spent 
on making a `cookiecutter`_ `package`_ by `pydanny`_ get integrated with `django-salted`_. 
This is now almost in a usable state. It requires a major clean up but for now will 
suffice for quickly getting projects off the ground. It allows me to simply type the 
following to get a new project started:

.. code-block:: sh
    
    $ cookiecutter https://github.com/usmanma/cookiecutter-django.git 
    ('answer a few questions about new project')
    $ cd new_project
    $ vagrant up

This will launch a :abbr:`VM (Virtual Machine)`, and provision it using Salt_. The end 
result will be a fully functional Django stack to begin work on.

Salt_ provisioning takes care of the following:

* nginx_ web server installation.
* Setup of nginx_ to proxy requests to uwsgi_.
* Installation of uwsgi_.
* Setup of uwsgi_ in Emperor_ mode with Django_ configuration.
* Installation of Postgresql_ database.
* Setup of Postgresql_ database by creating Django_ database and user.
* Installation of Python_ pip_ and virtualenv_.
* Creation of virtualenv_ for project.
* Installation of requirements including Django_ 1.6b with in virtualenv_.
* Configuration of Django_ to use the Postgresql_ database.

Although most of that was straight forward, making it work didn't work out as well.

The largest issue was with regards to requirement files calling other requirement files. 
No matter what was tried, Salt did not want to listen to any directory directives. 
Searching for a solution lead to this `question`_ on Stack Overflow. This was identical to 
the issue I was facing, and as is apparent, there was no solution at the time. After 
several attempts to resolve the issue, the answer I gave there (user: uzi) is what I had 
to do to get it working.

So now the only thing left to work out is why syncdb and migrate commands are not executing 
(and they aren't throwing any errors either).

Source code for this cookiecutter package can be found as usual on github_.

:icon:`time` Conclusion
-----------------------

Automating is hard work, and takes a long time. Hopefully it will pay off going forward.

Let's try to complete todays challenge for tomorrow now.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _package: https://github.com/pydanny/cookiecutter-django
.. _pydanny: https://github.com/pydanny
.. _django-salted: https://github.com/wunki/django-salted
.. _Salt: http://saltstack.com/
.. _nginx: http://nginx.org/
.. _uwsgi: https://github.com/unbit/uwsgi
.. _Emperor: http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html
.. _Postgresql: http://www.postgresql.org/
.. _Django: https://www.djangoproject.com/
.. _Python: http://python.org/
.. _pip: https://pypi.python.org/pypi/pip
.. _virtualenv: http://www.virtualenv.org/en/latest/
.. _question: http://stackoverflow.com/questions/18738238/salt-multiple-requirement-files-to-virtualenv
.. _github: https://github.com/usmanma/cc-django-salted