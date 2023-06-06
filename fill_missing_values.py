import pandas as pd
import print_csv_info

def fill_missing_values(df):
    while True:
        # ����ġ�� �ִ� �� ���
        columns_with_missing_values = df.columns[df.isnull().any()].tolist()
        print("����ġ�� �ִ� ��:")
        for column in columns_with_missing_values:
            print(column)

        # ����ڿ��� ����ġ ��ü�� �� ��ȣ �Է� �ޱ�
        columns_to_fill = input("����ġ�� ��ü�� �� ��ȣ�� �Է��ϼ��� (q = ������, 0���� ����, ���� ���� �ε��� �Է��� �������� ����): ").split()

        if 'q' in columns_to_fill:
            break

        # ������ �� �ε������� ��ȿ���� Ȯ��
        valid_indices = set(range(len(df.columns)))
        indices_to_fill = []
        for column_index in columns_to_fill:
            if column_index == 'q':
                break
            if int(column_index) not in valid_indices:
                print(f"��ȿ���� ���� �� ��ȣ�Դϴ�: {column_index}")
            else:
                indices_to_fill.append(int(column_index))

        # ����ڿ��� ����ġ ��ü ��� �Է� �ޱ�
        fill_method = input("����ġ�� ��ü�� ����� �����ϼ��� (1: �߾Ӱ�, 2: �ֺ� 3: ������): ")

        # ���õ� ���鿡 ���� ����ġ ��ü
        for column_index in indices_to_fill:
            column_name = df.columns[column_index]
            if fill_method == "1":
                # �߾Ӱ����� ��ü
                median_value = df[column_name].median()
                df[column_name].fillna(median_value, inplace=True)
            elif fill_method == "2":
                # �ֺ����� ��ü
                mode_value = df[column_name].mode()[0]
                df[column_name].fillna(mode_value, inplace=True)
                # ������ �� ����
            elif fill_method == '3':
                df1 = df
                df = df1.dropna()
                
            else:
                print(f"��ȿ���� ���� �����Դϴ�. �� {column_name}�� ����ġ ��ü�� �������� �ʽ��ϴ�.")

        # ������ CSV ���� ���� ���
        print_csv_info(df)

    return df