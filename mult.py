# Print multiplication table for numbers 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end='\t')
    print()  # Newline after each row

