from utilities import  read_util



test_invalid_login_data=[
        ("saul","saul123","Invalid credentials"),
        ("kim","kim123","Invalid credentials"),
        ("test","test123","Invalid credentials")
    ]


test_add_valid_employee_data=[
    ["Admin","admin123","John","J","Wick","John Wick","John"],
    ["Admin","admin123","Peter","J","Wick","Peter Wick","Peter"]
    ]

test_invalid_login_data=read_util.get_csv_as_list("../test_data/test_invalid_login_data.csv")


test_add_valid_employee_data=read_util.get_csv_as_list("../test_data/orange_test_data.xlsx")