from datetime import datetime

def greet_in_mandarin():
    current_hour = datetime.now().hour
    if 0 <= current_hour < 12:
        return "早上好"  # Good Morning
    elif 12 <= current_hour < 17:
        return "下午好"  # Good Afternoon
    else:
        return "晚上好"  # Good Evening

# Print the appropriate greeting
print(greet_in_mandarin())
