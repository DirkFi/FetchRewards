# Backend problem
## Introduction
This folder contains codes that can read the transactions from a CSV file & spend points based on the argument using the rules above and lastly return all payer point balances.

mycode.py is the mainly code, including the main function. test_mycode.py is the unit test, which can test some outlier values, for exmaple, when there is null value in the CSV file.
transactions.csv includes the original data that is listed in the question.
## Environment Setup
To run a Python code, you need to install Anaconda first in order to install more modules or pacakages more conveniently.
### Install Anaconda
Follow this [link](https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/) to install.

### Install Python environment
Use
```
conda create -n new_envir python=3.7 
```
to create a new virtual environment named new_envir.

Then
```
conda activate new_envir
```
to go into the new environment.
Then use
```
pip install pandas
``` 
to intall the package needed to run the code.

In the directory you put the code, use
```
python mycode.py 0
```
to run the code.

Remember to add some values at the end of the command, it can be any value but if it is not an integer which is greater than or equal to 0, it will cause errors.
By default, this command will use the transactions.csv to run the code, but if you want to test some random cases, feel free to change transactions.csv to satisfy
your needs. 

Or Use
```
python mycode.py 0 --csv_name YOUR_FILE_NAME
```
to run the code with your unique CSV file, remember to change YOUR_FILE_NAME to your unique file path.
