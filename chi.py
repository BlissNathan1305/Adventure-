import pytz
from datetime import datetime

def greet_in_mandarin():
    tz = pytz.timezone("Africa/Lagos")  # WAT timezone
    current_hour = datetime.now(tz).hour
    if 0 <= current_hour < 12:
        return "早上好"
    elif 12 <= current_hour < 17:
        return "下午好"
    else:
        return "晚上好"

print(greet_in_mandarin())
