# Professional Practice Assignment 1 
    Project Report
    Rishabh Patel

# Environment & Tools used
    OS- Windows 10
    Language- Python
    Verison- Python 3.6.1
    Testing Tools- pytest and pytest-cov

## Installation
*   [Python 3.6.1](https://www.python.org/downloads/release/python-361/)- This version was used to write 
    the code so it is recommended, but any Python 3 should work. 
    Make sure to check the "add python to path" option when installing.
    
    The code has been tested on Python 2.7.16 and all the tests will work. But, when using the
    CLI, make sure to enter all inputs surrounded by "" since the input function has been changed
    from Python 2 to Python 3.

    Install the required modules by entering the following lines into your command prompt
    
    ```bash
    pip install pytest
    pip install pytest-cov
    ```

# Executing the tests
    From a command prompt, go to the location of the test files you downloaded from github
    
    ```bash
    Example- cd C:\Users\Rishi\Downloads\PPA#1Python
    ```
    
    Below is an example of how to run a specific test from the command prompt. 
    Replace the filename with the name of the file you want to test. 
    In this example, it is running the tests in the file 'test_splitTip.py'
    
    ```
    pytest -rA test_splitTip.py
    ```
    
# Executing the command line interface
    From a command prompt, go to the location of the test files you downloaded from github
    
    ```
    Example- cd C:\Users\Rishi\Downloads\PPA#1Python
    ```
    
    Enter the line below in the command prompt to run the CLI
    
    ```
    
    python CommandLineApp.py
    
    ```
    
# Opinions on TDD
    I have done unit testing in java but it was very brief and a long time ago. This is the first time I am using TDD. 
    I definitely think unit testing is helpful in general, whether it be with TDD or not. For most software, unit testing is 
    probably necessary since there are many parts that need to be tested individually. 

    As for TDD, the main advantages I noticed for me were increased organization in code and minimal code. Writing the code, 
    I went in order of the tests, so everything just naturally grouped up like all the data type tests are grouped at the top. 
    Also, I only wrote code that was necessary to pass the tests so I didn't end up with any unused variables or useless lines. 

    The major drawback of TDD was slowness. For most of my functions, the test files had more lines of code than the function it was testing.
    To get a high code coverage, you need to write tests for simple code that you already know works and it just seems more like a formality to test it.
    In a real project, TDD's usefulness would depend on the project itself. If it was part of a large company where all the functions and 
    features are already specified and formalized, then I think TDD would be beneficial. If it was just a solo project or a small team, 
    I think it might be better for the flow of the project to jump right into the code.


"# PPA1_Rishabh_Patel" 
