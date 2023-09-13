import csv

def enclose_values_in_single_quotes(input_file):
    try:
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                quoted_values = [f"'{value}'" for value in row]
                print(', '.join(quoted_values) + ',')  # Add a comma at the end of each row
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")

if __name__ == "__main__":
    input_file = input("Enter the name of the CSV file: ")
    enclose_values_in_single_quotes(input_file)
