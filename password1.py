#Password Algorithm - Mr Harrison
import random # we need this to use randint

# set up lists
colours = ["Red","Blue","Green"]
animals = ["Tiger","Shark","Horse"]
puncs = ["%","£","&"]

# choose random values in lists
# randint(0,2) returns a random number 0,1,2
# NB. python counts from zero upwards!
colour = colours[random.randint(0, 2)]
animal = animals[random.randint(0, 2)]
punc = puncs[random.randint(0, 2)]

# make password and display it
password = colour + animal + punc
print("password =",password)





