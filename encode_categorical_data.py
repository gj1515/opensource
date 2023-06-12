import pandas as pd
from print_csv_info import print_csv_info


def encode_categorical_data(df):
    while True:
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        print("범주형 데이터 열:")
        for column in categorical_columns:
            print(column)

        # 사용자에게 범주형 데이터 열 번호 입력 받기
        columns_to_encode = input("범주형 데이터를 인코딩할 열 번호를 입력하세요 (q = 끝내기, 0부터 시작, 여러 개의 인덱스 입력은 공백으로 구분): ").split()

        if 'q' in columns_to_encode:
            break

        # 선택한 열 인덱스들이 유효한지 확인
        valid_indices = set(range(len(df.columns)))
        indices_to_encode = []
        for column_index in columns_to_encode:
            if int(column_index) not in valid_indices:
                print(f"유효하지 않은 열 번호입니다: {column_index}")
            else:
                indices_to_encode.append(int(column_index))

        # 선택된 열들에 대해 범주형 데이터 인코딩
        for column_index in indices_to_encode:
            column_name = df.columns[column_index]
            unique_values = df[column_name].unique().tolist()
            encoding_map = {value: index for index, value in enumerate(unique_values)}
            df[column_name] = df[column_name].map(encoding_map)

        # 수정된 CSV 파일 정보 출력
        print_csv_info(df)

    return df