def convert_currency_static(amount, from_currency, to_currency):
    # Hardcoded exchange rates (relative to USD, as of hypothetical date)
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "NGN": 1600.0
    }
    
    if from_currency not in rates or to_currency not in rates:
        return f"Error: Unsupported currency {from_currency} or {to_currency}"
    
    # Convert to USD first, then to target currency
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]
    return round(converted_amount, 2)

# Example usage
amount = 100
from_currency = "USD"
to_currency = "NGN"
result = convert_currency_static(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")
