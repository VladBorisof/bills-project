# Description

API service for working with the YaTube application


# Install
## How to start a project:
Clone the repository and change into it on the command line:

```
git clone https://github.com/VladBorisof/bills-project.git
```

# Start with Docker

```cd bills-project/bills && docker-compose up```

# Start without Docker

## Create and activate virtual environment:

```
cd bills-project

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip
```


## Install dependencies from requirements.txt file:

```pip install -r requirements.txt```

## Run migrations:

```python3 manage.py migrate```

## Run project:

```python3 manage.py runserver```

# Create new user

```POST http://127.0.0.1:8000/api/v1/users/```

with body

{
    "username": "test,
    "password": "strong_password",
}

After this ypu get token/ You need input token in Autorization

# Examples

run to get posts:

```GET http://127.0.0.1:8000/api/v1/bills/```

run to create posts:

```POST http://127.0.0.1:8000/api/v1/bills/```

with body

{
    "client_org": "OOO Client1Org1",
    "account_number": 1,
    "price": 10000,
    "date": "01.04.2021",
    "service": "вызов врача на дом",
    "client_name": "client1"
}




