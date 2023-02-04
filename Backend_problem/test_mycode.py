# Programmed by Dirk
# Time: 2023/2/3 17:48
from mycode import cal_result
import pandas as pd
import os


def test_mycode():
    # create test data
    # make it into A new csv file
    dt = pd.DataFrame({'payer': ['Name'], 'points': [100], 'timestamp': [None]})
    dt.to_csv("unit_test.csv", index=False)
    # check if the return value is correct
    assert cal_result("unit_test.csv") == 'There exists some NAN value in the csv file. Need to be checked before calculation.'
    assert cal_result("unit_test.csv", -1) == "You cannot spend money that is negative. Please check value."
    # delete the file that is created just now
    pwd = os.getcwd()
    os.remove(os.path.join(pwd, "unit_test.csv"))


if __name__ == '__main__':
    test_mycode()
