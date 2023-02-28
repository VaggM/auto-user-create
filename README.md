## Automated user creation from a spreadsheet

Create users from users.xlsx which has columns for First Name, Username, Password (not finals).

Mails will be created through automatically with @trustfirst.mobi and passwords will be automatically generated.

## Requirements

python3, pip and python venv module

## Setup

Within the auto-user-create folder

create a python venv

``` bash
python3 -m venv env
```
activate virtual environment

``` bash
source ./env/bin/activate
```

upgrade pip

``` bash
python -m pip install --upgrade pip
```

install required modules

``` bash
pip install -r requirements.txt
```

## Running

Activate the virtual environment if it isn't already up.

There are three python files available:

- dfprint.py

> prints out the data frame of the spreadsheet
>
> ``` bash
> python dfprint.py
> ``` 

- create.py

> creates users from the spreadsheet data frame
> and saves the output with the new passwords in passwords.txt
>
> ``` bash
> python create.py
> ```
>
> to check passwords.txt output run
>
> ``` bash
> cat passwords.txt
> ```

- read.py

> reads passwords.txt and writes all passwords to the spreadsheet data frame 
>
> ``` bash
> python read.py
> ```
