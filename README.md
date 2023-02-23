## Django Template for Railway, railway is a PaaS provider(similar to heroku/render) you get a container to run your app in the cloud.

### For a django app the flow is as follows, in the settings.py file: ``mysite.wsgi-> settings.py->static`` is what gets invoked when you run ``$>manage.py runserver``
### Dont forget to set your templates and media directories and your database, if you're using any.
 PostgreSQL is more than happy to overstay in RAM you may wanna check on that... hint: use sqlite for non-prod runs/tests.
 Ps: you're billed as per your resource utilization 
