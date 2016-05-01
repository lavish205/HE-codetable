# HE-codetable
Front End of [HackerEarth CodeTable](https://code.hackerearth.com) built using hackerearth APIs

### Project Setup
#### Installing Requirements
```shell
$ git clone git@github.com:lavish205/HE-codetable.git
$ cd HE-codetable
$ pip install -r requirements.txt
```
#### Setting up database
```mysql
# 1. Create the database named codetable:
create database codetable character;
# 2. Add a user
create user 'codetable'@'localhost' identified by 'codetable';
# 3. Set Permissions
grant all on codetable.* to 'codetable'@'localhost';
```
#### Run Migrations
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```
#### Run server
> $ python manage.py runserver 0.0.0.0:8000

Access panel at endpoint : [http://127.0.0.1:8000/hackerearth/code/](http://127.0.0.1:8000/hackerearth/code/)
