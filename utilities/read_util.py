import pandas

"""Method to convert csv file to list of list"""

def get_csv_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=";")
    return df.values.tolist()

"""Method to convert sheet into list of list"""

def get_sheet_as_list(file_path,sheet_name):
    df = pandas.read_csv(io=file_path,sheet_name=sheet_name)
    return df.values.tolist()
