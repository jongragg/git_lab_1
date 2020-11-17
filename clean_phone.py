import pandas as pd

def validate_phone(phone_number):
    bool_phone = phone_number.str.contains(r"^\d{3}[-]?\d{3}[-]?\d{4}")
    return bool_phone


numbers = pd.Series('784-890-0987','898-990-0023','dd-88-1000')
print(validate_phone(numbers))
