import os
import pandas as pd
from sqlalchemy import create_engine

# Configuration (update these values)
STORAGE_ACCOUNT_NAME = 'your_storage_account_name'
STORAGE_ACCOUNT_KEY = 'your_storage_account_key'
CONTAINER_NAME = 'your_container_name'
SQL_CONNECTION_STRING = 'your_sql_connection_string'

def process_cust_mstr(file_path):
    df = pd.read_csv(file_path)
    date_str = os.path.basename(file_path).split('_')[-1].split('.')[0]
    df['Date'] = pd.to_datetime(date_str, format='%Y%m%d').strftime('%Y-%m-%d')
    return df

def process_master_child(file_path):
    df = pd.read_csv(file_path)
    date_str = os.path.basename(file_path).split('-')[-1].split('.')[0]
    df['Date'] = pd.to_datetime(date_str, format='%Y%m%d').strftime('%Y-%m-%d')
    df['DateKey'] = date_str
    return df

def load_to_sql(df, table_name):
    engine = create_engine(SQL_CONNECTION_STRING)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    # List files in the data lake container (replace with actual implementation)
    files = [
        'path/to/CUST_MSTR_20191112.csv',
        'path/to/master_child_export-20191112.csv',
        'path/to/H_ECOM_ORDER.csv'
    ]

    for file_path in files:
        if 'CUST_MSTR' in os.path.basename(file_path):
            df = process_cust_mstr(file_path)
            load_to_sql(df, 'CUST_MSTR')
        elif 'master_child_export' in os.path.basename(file_path):
            df = process_master_child(file_path)
            load_to_sql(df, 'master_child')
        elif 'H_ECOM_ORDER' in os.path.basename(file_path):
            df = pd.read_csv(file_path)
            load_to_sql(df, 'H_ECOM_Orders')
