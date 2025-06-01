import random
import string

def generate_strong_password(length=12):
    if length < 4:  # Ensure length is enough for minimum requirements
        raise ValueError("Length must be at least 4 to include all character types.")
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure at least one of each
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest with random alphanumeric characters
    remaining_length = length - 4
    all_characters = lowercase + uppercase + digits + special
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

# Example usage
try:
    password = generate_strong_password(16)
    print("Generated Strong Password:", password)
except ValueError as e:
    print("Error:", e)
