def generate_pyramid(height):
    for i in range(1, height + 1):
        # Print leading spaces
        line = ' ' * (height - i)
        # Print stars
        line += '*' * (2 * i - 1)
        print(line)

# Example usage
height = 5
generate_pyramid(height)

