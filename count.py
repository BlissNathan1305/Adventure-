def count_down(end_number):
    """Counts down from 100 to the specified end number."""
    for i in range(100, end_number - 1, -1):
        print(i)

def main():
    while True:
        try:
            end_number = int(input("Enter the end number (less than or equal to 100): "))
            if end_number <= 100:
                count_down(end_number)
                break
            else:
                print("Please enter a number less than or equal to 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
