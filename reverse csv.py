import pandas as pd

# Load the CSV file
input_file = 'TW50.csv'
df = pd.read_csv(input_file)

# Reverse the rows
df_reversed = df.iloc[::-1]

# Save the reversed data to a new CSV file
output_file = 'TW50.csv'
df_reversed.to_csv(output_file, index=False)

print(f"Reversed CSV saved to '{output_file}'")
