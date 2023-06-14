import pandas as pd
from print_csv_info import print_csv_info
from remove_columns import remove_columns
from fill_missing_values import fill_missing_values
from encode_categorical_data import encode_categorical_data
from normalize_data import normalize_data
from set_column_as_index import set_column_as_index

def preprocess_titanic_data(input_file, output_file):
    # 1. 데이터셋 불러오기
    df = pd.read_csv(input_file)
    print_csv_info(df)
    
    while True:
        
        preprocess_data = input("실행할 기능을 선택하세요(q=끝내기, 1=열 제거, 2=결측치 대체, 3=범주형 데이터 인코딩, 4=데이터 정규화, 5=인덱스 번호 부여) ")
        if 'q' in preprocess_data:
            break

        # 열 제거
        if '1' in preprocess_data:
            df = remove_columns(df)

        # 결측치 대체
        if '2' in preprocess_data:
            df = fill_missing_values(df)

        # 범주형 데이터 인코딩
        if '3' in preprocess_data:
            df = encode_categorical_data(df)

        # 데이터 정규화 
        if '4' in preprocess_data:
            df = normalize_data(df)

        # 인덱스 번호 부여
        if '5' in preprocess_data:
            df = set_column_as_index(df)

    # 수정된 CSV 파일 저장
    df.to_csv(output_file, index=False)

    print("Training을 위한 CSV 파일 완성!")


# 함수 호출 
preprocess_titanic_data('./train.csv','./final.csv')