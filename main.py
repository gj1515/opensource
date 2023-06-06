import pandas as pd
import print_csv_info
import remove_columns
import fill_missing_values
import encode_categorical_data
import normalize_data
import set_column_as_index

def preprocess_titanic_data(input_file, output_file):
    # 1. �����ͼ� �ҷ�����
    df = pd.read_csv(input_file)

    print_csv_info(df)

    # �� ����
    df = remove_columns(df)

    # ����ġ ��ü
    df = fill_missing_values(df)

    # ������ ������ ���ڵ�
    df = encode_categorical_data(df)

    # ������ ����ȭ 
    df = normalize_data(df)

    # �ε��� ��ȣ �ο�
    df = set_column_as_index(df)

    # ������ CSV ���� ����
    df.to_csv(output_file, index=False)

    print("Training�� ���� CSV ���� �ϼ�!")

# �Լ� ȣ�� 
preprocess_titanic_data('./test.csv','./final.csv')