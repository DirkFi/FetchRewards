# Programmed by Dirk
# Time: 2023/2/3 16:35

import pandas as pd


if __name__ == '__main__':

    # csv_data = pd.read_csv("brands.csv", encoding='UTF-8')
    # df_selectd = csv_data.loc[:, ['BARCODE', 'BRAND_CODE', 'CATEGORY', 'NAME']]
    # df_selectd.to_csv("table_brand.csv", index=False)

    # csv_data = pd.read_csv("receipt_items.csv", encoding='UTF-8')
    # df_selectd = csv_data.loc[:, ['REWARDS_RECEIPT_ID', 'ITEM_INDEX', 'BARCODE', 'QUANTITY_PURCHASED', 'TOTAL_FINAL_PRICE']]
    # df_selectd.to_csv("Receipt_item.csv", index=False)

    # csv_data = pd.read_csv("receipts.csv", encoding='UTF-8')
    # df_selectd = csv_data.loc[:, ['ID', 'PURCHASE_DATE', 'DATE_SCANNED', 'TOTAL_SPENT', 'USER_ID']]
    # df_selectd.to_csv("Receipt.csv", index=False)

    csv_data = pd.read_csv("users.csv", encoding='UTF-8')
    df_selectd = csv_data.loc[:, ['ID', 'CREATED_DATE', 'BIRTH_DATE', 'GENDER', 'STATE']]
    df_selectd.to_csv("User.csv", index=False)