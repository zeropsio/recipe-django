# Zerops x Django

![django](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/cover-django.png)


[Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. This recipe aims to showcase a cloud-like integration of Django in [Zerops](https://zerops.io) through a simple file upload demo application.

<br />

## Deploy on Zerops
You can either click the deploy button to deploy directly on Zerops, or manually copy the [import yaml](https://github.com/zeropsio/recipe-django/blob/main/zerops-project-import.yml) to the import dialog in the Zerops app.

<a href="https://app.zerops.io/recipe/django">
    <img width="250" alt="Deploy on Zerops" src="https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/deploy-button.png">
</a>

<br/>
<br/>

## Recipe features

- **Load balanced** Django web app running on **Zerops Python** service
- Served by production-ready application server **[Gunicorn](https://gunicorn.org/)**
- Zerops **PostgreSQL 16** service as database
- Zerops **Object Storage** (S3 compatible) service as file system
- Automatic Django **database migrations**, **static files collection** and **superuser seeding**
- Utilization of Zerops built-in **environment variables** system
- **[Mailpit](https://github.com/axllent/mailpit)** as **SMTP mock server**
- **[Adminer](https://www.adminer.org)** for **quick database management** tool
- Unlocked development experience:
  - Access to database and mail mock through Zerops project VPN (`zcli vpn up`)
  - Prepared `.env.dist` file (`cp .env.dist .env` and change ***** secrets found in Zerops GUI)

<br/>

## Production vs. development

Base of the recipe is ready for production, the difference comes down to:

- Use highly available version of the PostgreSQL database (change `mode` from `NON_HA` to `HA` in recipe YAML, `db` service section)
- Use at least two containers for Django service to achieve high reliability and resilience (add `minContainers: 2` in recipe YAML, `app` service section)
- Use production-ready third-party SMTP server instead of Mailpit (change `MAIL_` secret variables in recipe YAML `app` service)
- Since the Django app will run behind our HTTP balancer proxy, add your domain/subdomains to `recipe/settings.py` `CSRF_TRUSTED_ORIGINS` setting or add `APP_DOMAIN` secret variable (in recipe YAML, `app` service section)
- Disable public access to Adminer or remove it altogether (remove service `adminer` from recipe YAML)

<br/>
<br/>

## Changes made over the default installation

If you want to modify your existing Django app to efficiently run on Zerops, these are the general steps we took:

- Add [zerops.yml](https://github.com/zeropsio/recipe-django/blob/main/zerops.yml) to your repository, our example includes idempotent migrations, static files collection and optimized build process
- Run `pip install django-storages` and change storage settings section in your `project/settings.py` to support S3 compatible Object Storage file system (more info [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html))
- Utilize Zerops [environment variables](https://github.com/zeropsio/recipe-django/blob/main/zerops.yml#L18-L30) and [secrets](https://github.com/zeropsio/recipe-django/blob/main/zerops.yml#L18-L30) to set up S3 for file system, database access, mailer and trusted hosts to work with reverse proxy load balancer
- Add init commands for your deployments to [migrate database and collect static images](https://github.com/zeropsio/recipe-django/blob/main/zerops.yml#L34-L39)

<br/>
<br/>

Need help setting your project up? Join [Zerops Discord community](https://discord.com/invite/WDvCZ54).
