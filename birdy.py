


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

		if selected == "1":
			print("Okay, let's make a New User Account")
			print("Enter your Full Name")
			full_name = input(">  ")
			print("Enter the Screen Name you would like to use")
			screen_name = input(">  ")

		if selected == "2":
			print("Please slecet your user")

		if selected == "3":
			print("1. View Public Chirps")
			print("2. View Private Chirps")
			chirp_pick = input("Which would you like to view?  ")

		if selected == "4":
			print("Get chirppin'!")
			new_chirp = input(">  ")

		if selected == "5":
			print("Please select the user you would like to chirp at")

		if selected == "6":
			exit()

