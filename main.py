import pandas as pd
import print_csv_info
import remove_columns
import fill_missing_values
import encode_categorical_data

def preprocess_titanic_data(input_file, output_file):
    # 1. 데이터셋 불러오기
    df = pd.read_csv(input_file)

    print_csv_info(df)

    # 열 제거
    df = remove_columns(df)

    # 결측치 대체
    df = fill_missing_values(df)

    # 범주형 데이터 인코딩
    df = encode_categorical_data(df)

    # 수정된 CSV 파일 저장
    df.to_csv(output_file, index=False)

    print("Training을 위한 CSV 파일 완성!")

# 함수 호출 예시
preprocess_titanic_data('./titanic.csv', './7titanic_final.csv')
