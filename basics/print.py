# The syntax for print is:
# print (<expression>)
print ("Hello World!")

# You can print multiple expressions, separated by commas:
print ("Hello", "World", "!")
print ("Sum of 2 and 3 is", 2 + 3) #Numbers can be printed without double quotes. They can be calculated directly.

# In the above example, the output is automatically separated by a space.
# You can change the separator using the 'sep' parameter:
print ("Hello", "World", "!", sep="-")
print ("2024", "06", "15", sep="/")
# You can also change the end character using the 'end' parameter:
print ("Hello", end="***")
print ("Goodbye", end="") # No newline at the end

