import csv

def enclose_values_in_brackets(input_file):
    try:
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                quoted_values = [f"'{value}'" for value in row]
                rows.append('(' + ', '.join(quoted_values) + ')')
            print(','.join(rows))  # Separate multiple rows with a comma
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")

if __name__ == "__main__":
    input_file = input("Enter the name of the CSV file: ")
    enclose_values_in_brackets(input_file)
