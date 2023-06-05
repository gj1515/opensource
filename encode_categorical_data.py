import pandas as pd
import print_csv_info


def encode_categorical_data(df):
    while True:
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        print("������ ������ ��:")
        for column in categorical_columns:
            print(column)

        # ����ڿ��� ������ ������ �� ��ȣ �Է� �ޱ�
        columns_to_encode = input("������ �����͸� ���ڵ��� �� ��ȣ�� �Է��ϼ��� (q = ������, 0���� ����, ���� ���� �ε��� �Է��� �������� ����): ").split()

        if 'q' in columns_to_encode:
            break

        # ������ �� �ε������� ��ȿ���� Ȯ��
        valid_indices = set(range(len(df.columns)))
        indices_to_encode = []
        for column_index in columns_to_encode:
            if int(column_index) not in valid_indices:
                print(f"��ȿ���� ���� �� ��ȣ�Դϴ�: {column_index}")
            else:
                indices_to_encode.append(int(column_index))

        # ���õ� ���鿡 ���� ������ ������ ���ڵ�
        for column_index in indices_to_encode:
            column_name = df.columns[column_index]
            unique_values = df[column_name].unique().tolist()
            encoding_map = {value: index for index, value in enumerate(unique_values)}
            df[column_name] = df[column_name].map(encoding_map)

        # ������ CSV ���� ���� ���
        print_csv_info(df)

    return df