# The syntax for getting user input is: 
name= input("What is your name? ")

# Sometimes we may need the input to be in a specific type, like integer or float.
# By default, input() returns a string. We can convert it using type conversion functions.
age =int(input("What is your age? ")) # Converting input to integer type
height =float(input("What is your height in meters? ")) # Converting input to float

# We can use it to do calculations
firstnumber= int(input("Enter the first number:"))
secondnumber= int(input("Enter the second number:"))
print ("The sum of", firstnumber, "and", secondnumber, "is", firstnumber + secondnumber)



# We can also do type conversion on already existing values.
num_str = "123"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

# We can also do concatenation after converting types
print ("The string '" + num_str + "' as an integer is " + str(num_int))
print ("The string '" + num_str + "' as a float is " + str(num_float))