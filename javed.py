import pandas as pd
from bioservices import UniProt

# Read the CSV file
df = pd.read_csv('file path')

# Print DataFrame columns to debug
print("DataFrame Columns:", df.columns)

# Print the first few rows of the DataFrame to inspect its contents
print("DataFrame Head:\n", df.head())

# Function to get protein sequence using UniProt
def get_protein_sequence(name):
    u = UniProt()
    try:
        results = u.search(name, columns="sequence", limit=1)
        if results:
            sequence = results.split('\n')[1]
            return sequence
        else:
            print(f"No results found for {name}")
            return None
    except Exception as e:
        print(f"Error retrieving sequence for {name}: {e}")
        return None

# Check if 'Name' column exists and apply function
if 'Name' in df.columns:
    df['Sequence'] = df['Name'].apply(get_protein_sequence)
    print("Protein sequences added to DataFrame.")
else:
    print("Column 'Name' does not exist in the DataFrame.")

# Print the updated DataFrame
print("Updated DataFrame Head:\n", df.head())

# Save the updated DataFrame to a new CSV file
df.to_csv('file path', index=False)
