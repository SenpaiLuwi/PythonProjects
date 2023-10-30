# function to add a record to the text file
def add_record():
    # get user input for Name, Email, and Home Address
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")
    address = input("Enter Home Address: ")
    # open the file in append mode and write the record
    with open("Record.txt", "a") as f:
        f.write(f"{name}\t\t{email}\t\t{address}\n")
    print("Record added successfully!")


# function to view all records from the text file
def view_records():
    try:
        with open("Record.txt", "r") as f:
            data = f.readlines()
            if len(data) == 0:
                print("No records found!")
            else:
                print("Name\t\t\t\t\t\tEmail\t\t\t\t\tAddress")
                for i, record in enumerate(data, start=1):
                    print(f"{i}. {record.strip()}")
    except FileNotFoundError:
        print("No records found!")


# function to clear all records from the text file
def clear_records():
    # open the file in write mode and clear all records
    with open("Record.txt", "w") as f:
        f.write("")
    print("All records cleared successfully!")


# main function to display options and execute selected task
def main():
    while True:
        print("\nRecord Keeping App")
        print("A. Add a Record")
        print("B. View All Records")
        print("C. Clear All Records")
        print("D. Exit")
        option = input("Enter option (A/B/C/D): ")
        if option.lower() == "a":
            add_record()
        elif option.lower() == "b":
            view_records()
        elif option.lower() == "c":
            clear_records()
        elif option.lower() == "d":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


# call the main function to start the app
if __name__ == "__main__":
    main()
