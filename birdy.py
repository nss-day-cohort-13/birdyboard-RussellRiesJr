


class Birdy():

	def show_options():
		print("1. New User Account")
		print("2. Select User")
		print("3. View Chirps")
		print("4. Public Chirps")
		print("5. Private Chirps")
		print("6. Exit")
		selected = input("Welcome to Birdyboard! What would you like to do?  ")

		if selected == "1":
			print("Okay, let's make a New User Account")

		if selected == "2":
			print("Please slecet your user")

		if selected == "3":
			print("1. View Public Chirps")
			print("2. View Private Chirps")
			chirp_pick = input("Which would you like to view?  ")

		if selected == "4":
			print("Viewing Public Chirps")

		if selected == "5":
			print("To view Private Chirps, select the user you would like to see")

		if selected == "6":
			