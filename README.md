# Installation

## Create environment

```sh
conda env create -f environment.yml --prefix ./venv
```

## Adjust settings

In **acc/settings/<dev|pre|prod>.py**, adjust settings to your application such as DB connection, email provider...

## Make migrations

If the secret key is not set in your system environment, you can set it before each launch:

```sh
SET SECRET_KEY="your_secret_key"
CALL activate ./venv
python manage.py makemigrations --settings=acc.settings.<dev|pre|prod>
python manage.py migrate --settings=acc.settings.<dev|pre|prod>
PAUSE
```

You can generate keys on [this website](https://djecrety.ir/).

# Running

**IMPORTANT**: this is not for deployment, but only development.

```sh
SET SECRET_KEY="your_secret_key"
CALL activate ./venv
python manage.py runserver --settings=acc.settings.<dev|pre|prod>
PAUSE
```