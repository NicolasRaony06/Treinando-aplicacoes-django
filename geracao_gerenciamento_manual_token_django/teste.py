from datetime import datetime, timedelta
from dataclasses import dataclass

# now = datetime.now()

# example_date = datetime.strptime("12-07-2024 10:00:00", "%d-%m-%Y %H:%M:%S")

# plus_15_min = now + timedelta(minutes=15)

# print(now)

# print('')

# print(plus_15_min)

# print(example_date)

# print('')

# print((plus_15_min - example_date))

@dataclass
class Token:
    date_conceived: datetime

def token_is_valid(token):
    conceived_token_data = token.date_conceived
    plus_15_min = conceived_token_data + timedelta(minutes=15)
    print(plus_15_min)
    now_date = datetime.now()

    return (plus_15_min >= now_date)

example_date = datetime.strptime("12-07-2024 10:25:00", "%d-%m-%Y %H:%M:%S")

token = Token(example_date)

print(token_is_valid(token))