import uuid


class Birdy():

	def show_options():
		print("1. New User Account")
		print("2. Select User")
		print("3. View Chirps")
		print("4. Public Chirps")
		print("5. Private Chirps")
		print("6. Exit")
		print("Welcome to Birdyboard! What would you like to do?")
		selected = input(">  ")
		current_user = None

		if selected == "1":
			print("Okay, let's make a New User Account")
			print("Enter your Full Name")
			full_name = input(">  ")
			print("Enter the Screen Name you would like to use")
			screen_name = input(">  ")
			current_user = screen_name

		if selected == "2":
			display_all_users()

		if selected == "3":
			print("1. View Public Chirps")
			print("2. View Private Chirps")
			chirp_pick = input("Which would you like to view?  ")

			if chirp_pick == "1":
				display_public_chirps()

			if chirp_pick == "2":
				display_private_chirp_users()

		if selected == "4":
			if current_user == None:
				print("You must select a select a Screen Name before you can chirp")
				display_all_users()
			else:
				print("Get chirppin'!")
				new_chirp = input(">  ")

		if selected == "5":
			if current_user == None:
				print("You must select a select a Screen Name before you can view private chirps")
				display_all_users()
			else:
				display_private_chirp_users()

		if selected == "6":
			exit()


	def display_all_users():
		print("Please slecet your user")

	def display_private_chirp_users():
		print("Please select the user you would like to chirp at")

	def display_public_chirps():