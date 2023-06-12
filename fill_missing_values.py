import pandas as pd
from print_csv_info import print_csv_info

def fill_missing_values(df):
    while True:
        # 결측치가 있는 열 출력
        columns_with_missing_values = df.columns[df.isnull().any()].tolist()
        print("결측치가 있는 열:")
        for column in columns_with_missing_values:
            print(column)

        # 사용자에게 결측치 대체할 열 번호 입력 받기
        columns_to_fill = input("결측치를 대체할 열 번호를 입력하세요 (q = 끝내기, 0부터 시작, 여러 개의 인덱스 입력은 공백으로 구분): ").split()

        if 'q' in columns_to_fill:
            break

        # 선택한 열 인덱스들이 유효한지 확인
        valid_indices = set(range(len(df.columns)))
        indices_to_fill = []
        for column_index in columns_to_fill:
            if column_index == 'q':
                break
            if int(column_index) not in valid_indices:
                print(f"유효하지 않은 열 번호입니다: {column_index}")
            else:
                indices_to_fill.append(int(column_index))

        # 사용자에게 결측치 대체 방법 입력 받기
        fill_method = input("결측치를 대체할 방법을 선택하세요 (1: 중앙값, 2: 최빈값 3: 행제거): ")

        # 선택된 열들에 대해 결측치 대체
        for column_index in indices_to_fill:
            column_name = df.columns[column_index]
            if fill_method == "1":
                # 중앙값으로 대체
                median_value = df[column_name].median()
                df[column_name].fillna(median_value, inplace=True)
            elif fill_method == "2":
                # 최빈값으로 대체
                mode_value = df[column_name].mode()[0]
                df[column_name].fillna(mode_value, inplace=True)
                # 결측지 행 제거
            elif fill_method == '3':
                df1 = df
                df = df1.dropna()
                
            else:
                print(f"유효하지 않은 선택입니다. 열 {column_name}의 결측치 대체를 수행하지 않습니다.")

        # 수정된 CSV 파일 정보 출력
        print_csv_info(df)

    return df