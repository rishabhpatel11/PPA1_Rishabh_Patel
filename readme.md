# Professional Practice Assignment 1 
Project Report
Rishabh Patel

# Naming Conventions
Each function has a testing file associated with it. Pytest requires 'test_' before or after
the file name and individual unit test name. I decided to put the keyword in the front so the test files 
are named as such: 'test_bmi'. Individual unit tests also follow the format of 'test_'+'NameOfTest'.

Pytest doesn't allow a descriptor for tests so I tried to keep the test names as descriptive as possible
to fill this void. The two types of tests I used are ones that assert whether something is true or
ones that check whether a specific error/exception is raised. The names indicicate whether it was testing for
success or failure.

# Environment & Tools used
OS- Windows 10
Language- Python 3.6.1
Testing Tools- pytest 
Coverage Tool- pytest-cov

## Installation
*   [Python 3.6.1](https://www.python.org/downloads/release/python-361/)- This version was used to write 
the code so it is recommended, but any Python 3 should work. 
Make sure to check the "add python to path" option when installing.

If you already have a version of Python 2 installed, the code should still work but for the
CLI, make sure to enter all inputs surrounded by "" since the input function has been changed
from Python 2 to Python 3.

Install the required modules by entering the following lines into your command prompt

```bash
pip install pytest
pip install pytest-cov
```

The full list of required modules includes py and pluggy but those should be installed already.

# Executing the tests
From a command prompt, go to the location of the test files you downloaded from github

```bash
Example- cd C:\Users\Rishi\Downloads\PPA#1Python
```

To run all test files and see the results of each individual unit test, use the
following command:

    pytest -rA

Below is an example of how to run a specific test from the command prompt. 
Replace the filename with the name of the file you want to test. 
In this example, it is running the tests in the file 'test_splitTip.py'

```bash
pytest -rA test_splitTip.py
```

# Executing the command line interface
From a command prompt, go to the location of the test files you downloaded from github

```bash
Example- cd C:\Users\Rishi\Downloads\PPA#1Python
```

Enter the line below in the command prompt to run the CLI

```bash
python CommandLineApp.py
```

# Opinions on TDD
I haved used unit testing in java but it was a long time ago and very brief. For my first time unit testing in python, I found it
to be fairly straightforward and simple. Each test was logically understandable and only required a few lines to set up.
This is the first time I am using TDD. I would say TDD was helpful to make sure my functions fulfilled the requirements, but
it was also a little annoying to deal with, when sometimes I write a test for what ends up being not even a full line of code.
I definitely think unit testing is helpful in general, whether it be with TDD or not. For most software, unit testing is 
probably necessary since there are many parts that need to be tested individually. 

For TDD, the main advantages I noticed for me were increased organization in code and minimization of code. Writing the code, 
I went in order of the tests, so everything just naturally grouped up like all the data type tests are grouped at the top. 
Also, I only wrote code that was necessary to pass the tests so I didn't end up with any unused variables or useless lines. 

The major drawback of TDD was slowness. For most of my functions, the test files had more lines of code than the function it was testing.
To get a high code coverage, you need to write tests for simple code that you already know works and it just seems more like a formality to test it.
The other big disadvantage I ran into was having tests cause other tests to fail. One test requires a certain change, like changing my output type 
from a number to a string. Then, I would have to go through the other tests and change them as well.

In a real project, TDD's usefulness would depend on the project itself. If it was part of a large company where all the functions and 
features are already specified and formalized, then I think TDD would be beneficial. If it was just a solo project or a small team, 
I think it might be better for the flow of the project to jump right into the code. 


"# PPA1_Rishabh_Patel" 
