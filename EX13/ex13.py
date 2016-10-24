from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# It appear ValueError: need more than 3 values to unpack when the input is less than 3
# Because the "third" string doesn't contain anything if the user doesn't type anything to it
