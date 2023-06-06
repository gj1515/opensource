import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data(df):
    while True:
        # 사용자에게 정규화할 열 번호 입력
        column_number = input("정규화할 열 번호를 입력하세요 (q=끝내기, 0부터 시작, 여러 개의 인덱스 입력은 공백으로 구분): ").split(' ')

        if 'q' in column_number:
            break

        # 유효한 열 번호인지 확인
        columns_index = []
        for number in column_number:
            if int(number) not in range(len(df.columns)):
                print(f"유효하지 않은 열 번호입니다: {number}")
                continue
            else :
                columns_index.append(int(number))
        
        # 데이터 정규화하기
        scaler = MinMaxScaler()
        for index in columns_index :
            column_name = df.columns[int(index)]
            df[[column_name]] = scaler.fit_transform(df[[column_name]])
        
        return df