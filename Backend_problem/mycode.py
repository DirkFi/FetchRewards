# Programmed by Dirk
# Time: 2023/2/3 16:35

import pandas as pd
import argparse
from collections import deque


def cal_result(file_name, value=0):
    # value needs to be positive
    if value < 0:
        return "You cannot spend money that is negative. Please check value."
    # read data
    csv_data = pd.read_csv(file_name, encoding='UTF-8')
    # check if there is any NAN value in the csv file
    if csv_data.isnull().any().any():
        return "There exists some NAN value in the csv file. Need to be checked before calculation."
    payer_set = set()
    money_list = deque()
    csv_data = csv_data.sort_values(by=['timestamp'])
    # add the spending value to the dataframe
    csv_data.loc[csv_data.shape[0]] = ['', -value, '']

    for i in range(csv_data.shape[0]):
        payer = csv_data.iloc[i]['payer']
        # if not the spending case
        if i != csv_data.shape[0]-1:
            # add those payers whose money has been used out
            if payer not in payer_set:
                payer_set.add(payer)
        val = csv_data.iloc[i]['points']
        # add money
        if val > 0 and i != csv_data.shape[0]-1:
            money_list.append([payer, val])

        # i == csv_data.shape[0]-1 and val < 0
        # is ruled out

        # spend money
        elif val < 0:
            val = -val
            while len(money_list) > 0 and val > 0:
                if money_list[0][1] <= val:
                    val -= money_list[0][1]
                    money_list.popleft()
                else:
                    money_list[0][1] -= val
                    val -= val
            if val > 0 and len(money_list) == 0:
                return "There is not enough money. Please double check."
    # final result
    result = dict()
    for name, va in money_list:
        if name not in result:
            result[name] = va
        else:
            result[name] += va
    # add missing payer with num 0
    for name in payer_set:
        if name not in result:
            result[name] = 0

    return result


if __name__ == '__main__':
    # add arguments
    parser = argparse.ArgumentParser(description='Begin calculation')
    parser.add_argument('value', type=int, default=0)
    parser.add_argument('--csv_name', type=str, default='transactions.csv')
    args = parser.parse_args()

    print(cal_result(args.csv_name, args.value))
