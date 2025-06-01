import math
import pandas as pd

def generate_log_table_advanced(start, end, step=1, custom_base=None, decimals=4, output_file=None):
    # Initialize lists for table data
    numbers = []
    ln_values = []
    log10_values = []
    log2_values = []
    custom_log_values = []
    
    # Generate data
    for x in range(start, end + 1, step):
        numbers.append(x)
        if x == 0:
            ln_values.append("undefined")
            log10_values.append("undefined")
            log2_values.append("undefined")
            custom_log_values.append("undefined")
        else:
            ln_values.append(round(math.log(x), decimals))
            log10_values.append(round(math.log10(x), decimals))
            log2_values.append(round(math.log2(x), decimals))
            if custom_base:
                custom_log_values.append(round(math.log(x, custom_base), decimals))
            else:
                custom_log_values.append("-")
    
    # Create DataFrame
    columns = ["Number", "ln(x)", "log10(x)", "log2(x)"]
    data = {
        "Number": numbers,
        "ln(x)": ln_values,
        "log10(x)": log10_values,
        "log2(x)": log2_values
    }
    if custom_base:
        columns.append(f"log{custom_base}(x)")
        data[f"log{custom_base}(x)"] = custom_log_values
    
    df = pd.DataFrame(data, columns=columns)
    
    # Print table
    print(df.to_string(index=False))
    
    # Save to file if specified
    if output_file:
        df.to_csv(output_file, index=False)
        print(f"\nTable saved to {output_file}")

# Example usage
generate_log_table_advanced(1, 5, step=1, custom_base=5, decimals=4, output_file="log_table.csv")
