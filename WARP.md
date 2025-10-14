# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project overview
- Stack: Django (5.x), Python 3.x. Minimal template with two Django apps: core and item
- Entry points: manage.py sets DJANGO_SETTINGS_MODULE=configuration_root.settings; configuration_root contains settings.py and urls.py
- Default DB: SQLite (db.sqlite3). A Postgres service is defined in docker-compose.yml but not wired by default in settings
- Debug tooling: django-debug-toolbar is installed and enabled (DebugToolbarMiddleware + debug_toolbar_urls)
- Templates/Assets: templates at django_project_root/templates/, static at django_project_root/static/, media at django_project_root/media/

Common commands
- Environment setup (from README.md)
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt

- Database
  - Initialize/migrate: python manage.py migrate
  - Create superuser: python manage.py createsuperuser

- Run the dev server
  - python manage.py runserver
  - Default app routes:
    - / → django_project_root.core.urls (home, auth pages)
    - /items/ → django_project_root.item.urls (item detail and creation)

- Tests
  - Run all tests: python manage.py test
  - Run tests in one app/module: python manage.py test django_project_root.core.tests
  - Run a single test (pattern): python manage.py test django_project_root.core.tests.YourTestCase.test_method

- Lint/format
  - No linter/formatter configuration is present in this repo (no ruff/flake8/black config files detected)

- Docker (optional)
  - Build image: docker build -t django-market-place .
  - Run container: docker run --rm -p 8000:8000 django-market-place
  - docker-compose.yml includes a Postgres service. To use Postgres, you’ll need to adapt configuration_root/settings.py (e.g., via env vars) before enabling a web service in compose

High-level architecture
- Django project layout
  - manage.py: CLI entry for Django management commands
  - configuration_root/
    - settings.py: INSTALLED_APPS includes django_project_root.core, django_project_root.item, and debug_toolbar; DEBUG=True by default; SQLite DB; template/static/media dirs configured; auth login/logout redirects set
    - urls.py: route root to core.urls, /items/ to item.urls, /admin/ to Django admin; appends debug_toolbar_urls and serves MEDIA in development
  - django_project_root/
    - core/ (app):
      - views: index (lists items and categories), contact, signin/signup flows (signin uses Django’s LoginView with custom form; signup saves a user via SignUpForm)
      - forms: SignUpForm extends UserCreationForm; SignInForm extends AuthenticationForm (both with styled widgets)
      - urls: namespaced as core; routes '', signup/, signin/, contact/
    - item/ (app):
      - models: Category and Item. Item relates to Category and auth.User; includes created_at and created_by
      - views: detail (shows item and related items), new (login_required; creates Item via NewItemForm assigning created_by)
      - forms: NewItemForm ModelForm for Item
      - urls: namespaced as item; routes <int:pk> and new/

Notes for future agents
- The repository currently uses SQLite for simplicity; docker-compose defines Postgres but the Django settings default to SQLite. If switching to Postgres, update DATABASES accordingly (or use an env-driven settings pattern) before enabling a web service in compose
- Debug Toolbar is active in development (DEBUG=True and INTERNAL_IPS includes 127.0.0.1). Ensure INTERNAL_IPS is correctly set if accessing via containers/network
- Tests stubs exist in core/tests.py and item/tests.py; add real tests as you extend functionality
