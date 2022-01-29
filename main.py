#create a variable to hold the quantity of seats left available on a flight
available_seats = 60
#create a variable to hold the cost of groceries at checkout
grocery_total = 48.65
#create a variable to hold a person's middle initial
middle_initial = "R"
#create a variable to hold true if its hot outside and false if its cold outside
is_it_hot_outside = False
#create a variable to hold a person's first name
first_Name = "Sean"
#create a variable to hold a street address
street_address = "Clocktower Place"
#print all variables to the console
print("Seats available on the plane: " + str(available_seats)) # you have to convert an int to a string to concatenate
print("$" + str(grocery_total))
print("Middle initial: " + str(middle_initial))
print("Is it hot outside? " + str(is_it_hot_outside))
print("First name: " + str(first_Name))
print("Street address: " + str(street_address))
#a customer has booked 2 planes tickets. remove two seats
available_seats -= 2
print("Seats available on the plane: " + str(available_seats))
#impulse candy bar purchase, add 2.15 to the total
grocery_total += 2.15
print("$" + str(grocery_total))
#birth certificate was printed incorrectly, change the middle initial to something else
middle_initial = "Q"
print("Middle initial: " + str(middle_initial))
#the season has changed, update the hot variable to the opposite of what it was
is_it_hot_outside = True
print("Is it hot outside? " + str(is_it_hot_outside))
#create a new variable of the person's full name using the first name, middle initial, and a last name of your choice
full_name = first_Name + " " + middle_initial + " Jameson"
print(full_name)
#print a line introducing a customer and says they live at the address variable
print("Hi, my name is " + full_name + ", and live on " + street_address + ".")