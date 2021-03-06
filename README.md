# Planning Poker Backend

[Frontend Repo](https://www.github.com/SimonAlmers/planningpoker-fe)

# [API Documentation](./docs/api/endpoints.md)

# Setup

Clone backend repo into `project` directory

```bash
git clone git@github.com:SimonAlmers/planningpoker-be.git project
```

Create virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

Change into the `project` directory

```bash
cd project
```

Add `.env` file in the root of the project dir

```bash
touch .env
```

Add env variables to `.env` file:

The value for the `FIREBASE_URL` will be explained in the [Firebase Realtime Database Setup](https://github.com/SimonAlmers/planningpoker-fe/blob/main/docs/FIREBASE_SETUP.md)

```bash
export SECRET_KEY='***' # Generate Django Secret here:
export DATABASE_URL='postgres://[user]:[password]@localhost/[database_name]' # Postgres Database URL (not needed if using development- or test-settings which uses sqlite)
export FIREBASE_URL='***'
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run migrations on your local database

```bash
python manage.py migrate --settings config.settings.development
```

Create a superuser to be able to login to the django admin.

```bash
python manage.py createsuperuser --settings config.settings.development
```

Collect static files

```bash
python manage.py collectstatic --settings config.settings.development
```

Spin up a development server on localhost port `8080`

```bash
python manage.py runserver 0:8080 --settings config.settings.development
```

# Visit the Django Admin

## [Django Admin](http://localhost:8080/admin/)

## [API Docs](http://localhost:8080/docs/)

# Test

```bash
python manage.py test --settings config.settings.test
```

or

```bash
python manage.py test --pattern="test_*.py" --settings config.settings.test
```
