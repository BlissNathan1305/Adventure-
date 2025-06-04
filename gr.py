def greet(name, time_of_day=None):
    if time_of_day is None:
        return f"Hello, {name}!"
    elif time_of_day == "morning":
        return f"Good morning, {name}!"
    elif time_of_day == "afternoon":
        return f"Good afternoon, {name}!"
    elif time_of_day == "evening":
        return f"Good evening, {name}!"
    else:
        return f"Hello, {name}!"

# Example usage:
print(greet("John"))  # Output: Hello, John!
print(greet("John", "morning"))  # Output: Good morning, John!
print(greet("John", "afternoon"))  # Output: Good afternoon, John!
print(greet("John", "evening"))  # Output: Good evening, John!
