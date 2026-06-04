#Mini Project
#Contact Book
contacts = {}
while True :
	print("1. View Contacts")
	print("2. Add Contact ")
	print("3.Search Contact")
	print("4.Exit")
	
	choice = input("Enter your choice(1-4)):")
	
	if choice == "1":
	   print(f"contacts list {contacts}")
	
	elif choice == "2":
		 name = input("Enter contact name: ")
		 phone_number = input("Enter phone number: ")
		 contacts[name]=phone_number
		 print(f"contact add successfuly . new contacts {contacts }")
	elif choice == "3":
		  name = input("Enter name to Search")
		  if name in contacts:
			 print(contacts[name])
		  else:
			print("Contact not found.")
	elif choice =="4":
		   print("contacts completed ")
		   break
		

	 

   
