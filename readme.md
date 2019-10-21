# Professional Practice Assignment 2
Project Report

Rishabh Patel

# Naming Conventions
Each function has a testing file associated with it. Pytest requires 'test_' before or after
the file name and individual unit test name. I decided to put the keyword in the front so the test files 
are named as such: 'test_bmi'. Individual unit tests also follow the format of 'test_'+'NameOfTest'.

# Environment & Tools used
OS- Windows 10

Language- Python 3.6.1

Testing Tools- pytest 

Coverage Tool- pytest-cov

Database- Docker MYSQL

CI Tool- Travis CI

## Installation
*   [Python 3.6.1](https://www.python.org/downloads/release/python-361/)- This version was used to write 
the code so it is recommended, but any Python 3 should work. 
Make sure to check the "add python to path" option when installing.
*   [Docker](https://www.docker.com/products/docker-desktop)

Install the required modules by entering the following lines into your command prompt

```bash
pip install sqlalchemy
pip install pymysql
pip install prettytable
pip install flask
pip install flask_mysqldb
pip install pytest
pip install mock
pip install doubles
```

The full list of required modules includes py and pluggy but those should be installed already.

# Executing the tests
Make sure docker desktop is running

Execute the following commands to set up the database in docker:
```bash
        docker run --name=rp_mysql --env="MYSQL_ROOT_PASSWORD=password" -p 3308:3306 -d mysql:latest
	docker exec -it rp_mysql mysql -uroot -ppassword    (Note: For some reason, you have to right click to paste instead of CRTL+v)
	create database ppa2;
	use ppa2;
	CREATE TABLE distances_table (x1 float, y1 float, x2 float, y2 float, distance float, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
	CREATE TABLE bmi_table (feet int, inches int, weight float, BMI float,category varchar(50), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
	CREATE TABLE web_requests(IP varchar(50), request varchar(50), requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
	exit;
```
# How to run the command line app (including the web app)
From a command prompt, go to the location of the test files you downloaded from github

```bash
Example- cd C:\Users\Rishi\Downloads\PPA#1_Rishabh_Patel_
```

Execute the following 

```bash
python main.py
```
# How to view web requests database

```bash
docker exec -it rp_mysql mysql -uroot -ppassword
use ppa2;
select * from web_requests;
```

# How to run all tests

```bash
pytest -rA
```

# How to run a single test

```bash
pytest -rA test_database.py
```

# Screencast of final CI
![final CI](https://github.com/rishabhpatel11/PPA1_Rishabh_Patel/blob/master/GIFs%2BImages/Phase4/CI_phase4.gif)

# CLI Database Functionality
![final CI](https://github.com/rishabhpatel11/PPA1_Rishabh_Patel/tree/master/GIFs%2BImages/Phase2/databaseFunctionality.gif)

# Web App Functionality
![final CI](https://github.com/rishabhpatel11/PPA1_Rishabh_Patel/blob/master/GIFs%2BImages/Phase3/webFunctionality.gif)

# Test Output Report
Code used to create the test output:

```
    pytest -rA
```

![test report](https://github.com/rishabhpatel11/PPA1_Rishabh_Patel/blob/master/GIFs%2BImages/Phase4/testoutput.JPG)

# Test Coverage Report
Code used to create the coverage report:

```
    pytest --cov
```

![coverage report](https://github.com/rishabhpatel11/PPA1_Rishabh_Patel/blob/master/GIFs%2BImages/Phase4/coveragereport.JPG)



"# PPA2_Rishabh_Patel" 
