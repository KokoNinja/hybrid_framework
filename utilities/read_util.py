import pandas

def get_csv_as_list():
    df = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")
    return df.values.tolist()
