def gallon_to_liter(gallon):
    liter = gallon * 3.78541
    return liter

gallon = float(input("Enter volume in gallons: "))
liter = gallon_to_liter(gallon)

print(f"{gallon} gallon(s) is equal to {liter:.2f} liters.")
