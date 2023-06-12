import pandas as pd
from print_csv_info import print_csv_info

def remove_columns(df):
    while True:
        # 사용자에게 제거할 열 인덱스 입력 받기
        columns_to_remove = input("제거할 열 번호를 입력하세요 (q=끝내기, 0부터 시작, 여러 개의 인덱스 입력은 공백으로 구분): ").split()

        if 'q' in columns_to_remove:
            break

        # 선택한 열 인덱스들이 유효한지 확인
        valid_indices = set(range(len(df.columns)))
        indices_to_remove = []
        for column_index in columns_to_remove:
            if int(column_index) not in valid_indices:
                print(f"유효하지 않은 열 번호입니다: {column_index}")
            else:
                indices_to_remove.append(int(column_index))

        # 선택된 열들 제거
        removed_columns = [df.columns[column_index] for column_index in indices_to_remove]
        df = df.drop(columns=removed_columns)
        print(f"제거된 열: {', '.join(removed_columns)}")

        # 수정된 CSV 파일 정보 출력
        print_csv_info(df)

    return df