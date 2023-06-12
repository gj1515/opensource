import pandas as pd

def set_column_as_index(df):
    while True:
        # 사용자에게 인덱스로 사용할 열 번호 입력받기
        column_number = input("인덱스로 사용할 열 번호를 입력하세요 (q=끝내기, 0부터 시작): ")

        if 'q' in column_number:
            break

        # 유효한 열 번호인지 확인
        if int(column_number) not in range(len(df.columns)):
            print(f"유효하지 않은 열 번호입니다: {column_number}")
            continue

        # 선택한 열을 인덱스로 사용
        column_name = df.columns[int(column_number)]
        df.set_index(column_name, inplace=True)
        print(f'인덱스로 사용된 열 : {column_name}')

        return df