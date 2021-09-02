# Aviyel.ConferenceManagement.CoreAPI

Backend to create and manage conferences in the world of Remote Culture


# Project Requirements
- Postgres DB
- Python 3.9 or Higher
- Install requirements from Requirements.txt file
## Spinning the Server

`python manage.py runserver`

** Please make sure the Migration Scripts are generated and migrate command is executed once you configure your DB. Necessary commands are instructed below


### Managing Environment Variables

An environment file needs to be created in the Project folder as `.env`
Inside this file please add the following data to configure your the project with your Database

```
DATABASE_NAME = <DB_NAME>
DATABASE_USER = <DB_USERNAME>
DATABASE_PASSWORD = <DB_USER_PASSWORD>
```

- `<`, `>` are to be excluded ^^

## Database Credentials that needs to be added in the .env file

## Creating virtual env for the project

`python -m venv .venv`

Install the requirements using ` pip install -r requirements.txt`

## Attach pre-commit to project using the following command

`pre-commit install`

# Database Related Operations

## Migrations

Generate the migration files

`python manage.py makemigrations`

Migrate the schema to Database

`python manage.py migrate`
