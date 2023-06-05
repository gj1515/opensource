import pandas as pd
import print_csv_info

def remove_columns(df):
    while True:
        # ����ڿ��� ������ �� �ε��� �Է� �ޱ�
        columns_to_remove = input("������ �� ��ȣ�� �Է��ϼ��� (q=������, 0���� ����, ���� ���� �ε��� �Է��� �������� ����): ").split()

        if 'q' in columns_to_remove:
            break

        # ������ �� �ε������� ��ȿ���� Ȯ��
        valid_indices = set(range(len(df.columns)))
        indices_to_remove = []
        for column_index in columns_to_remove:
            if int(column_index) not in valid_indices:
                print(f"��ȿ���� ���� �� ��ȣ�Դϴ�: {column_index}")
            else:
                indices_to_remove.append(int(column_index))

        # ���õ� ���� ����
        removed_columns = [df.columns[column_index] for column_index in indices_to_remove]
        df = df.drop(columns=removed_columns)
        print(f"���ŵ� ��: {', '.join(removed_columns)}")

        # ������ CSV ���� ���� ���
        print_csv_info(df)

    return df