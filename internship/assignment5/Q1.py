#Q1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.
import csv

def create_csv_file( filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Mobile', 'Email'])  # Write the header


def insert_dummy_data( filename):
    with open(filename  , mode='a', newline='') as file:
        writer = csv.writer(file)
        for _ in range(3):  # Insert 3 dummy data entries
            name = input("Enter name: ")
            address = input("Enter address: ")
            mobile = input("Enter mobile: ")
            email = input("Enter email: ")
            writer.writerow([name, address, mobile, email])  # Write the data row

# Example usage:
create_csv_file("address_book.csv")
insert_dummy_data("address_book.csv")