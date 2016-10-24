my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 75 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'Whit'
my_hair = 'Brown'

# %d is for decimal numbers
# %s is for strings
# %r is for all


print "Let's talk about about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_height
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " %(my_age, my_height, my_weight, my_age + my_height + my_weight)
