import pandas as pd

def print_csv_info(df):
    print("CSV 파일 정보:")
    print(df.info())
    print(df.head())