names = []
contact_numbers = []
agree = 'y'
while agree == 'y':
    choice = int(input("Select an operation you want \n1.Adding a contact \n2.Deleting a contact \n3.Search an Contact"))
    if choice == 1:
        num = int(input("Enter the total number of contacts you want to save: "))
        for i in range(num):
            name = input("Name: ")
            contact_number = int(input("Contact Number: ")) 
            names.append(name)
            contact_numbers.append(contact_number)
        print("\nName\t\t\tContact Number\n")
        for i in range(num):
            print("{}\t\t\t{}".format(names[i], contact_numbers[i]))
    elif choice == 2:
        del_item_choice = input("Enter the name/contact number (only write contact)of the person to delete")
        if del_item_choice in names :
            index = names.index(del_item_choice)
            x=names.pop(index)
            y=contact_numbers.pop(index)
            print(f"The person with{x} with contact {y} has been removed")

        elif del_item_choice in contact_numbers:
            index = contact_numbers.index(del_item_choice)
            x=names.pop(index)
            y=contact_numbers.pop(index)
            print(f"The person with{x} with contact {y} has been removed")
        else:
            print("not found, can't delete")
        

            
    elif choice == 3:
        search_term = input("\nEnter search term: ")
        print("Search result:")
        if search_term in names:
            index = names.index(search_term)
            contact_number = contact_numbers[index]
            print("Name: {}, Phone Number: {}".format(search_term, contact_number))
        else:
            print("No Records") 

    else:
        print("Invalid input")
    agree = input("do you want to have another operation?[y/n]")
    
