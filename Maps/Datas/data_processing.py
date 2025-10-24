import csv

# Open the CSV file
with open("Communes.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Read as dictionary
    columns = reader.fieldnames  # Get column names


# Input and output file names
input_file = "communes_modifie8.csv"
output_file = "communes_modifie9.csv"
column_to_remove = 'code_region'  # Name of the column to delete

# Read and modify the CSV
with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Read as dictionary
    columns = [col for col in reader.fieldnames if col != column_to_remove]  # Remove target column
    
    with open(output_file, "w", newline='', encoding='utf-8') as csvfile_mod:
        writer = csv.DictWriter(csvfile_mod, fieldnames=columns)  # Write updated columns
        writer.writeheader()  # Write column names
        for row in reader:
            del row[column_to_remove]  # Remove the column from each row
            writer.writerow(row)  # Write modified row

print(f"The file {output_file} has been created without the column '{column_to_remove}'.")
