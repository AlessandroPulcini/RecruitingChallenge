from Utils import EvenStream
from decimal import Decimal as D

# Task 11
def calculate_cost(duration_in_seconds):
    minute_rate = D("1.45")
    temp_duration_in_seconds = D(str(duration_in_seconds))
    seconds_in_minute = D("60")
    cost = minute_rate * temp_duration_in_seconds / seconds_in_minute
    return float(cost)


# Task 12
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    output = []
    for _ in range(n):
        output.append(stream.get_next())
    return output
