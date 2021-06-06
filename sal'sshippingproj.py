# The Python sys module provides access to any command-line arguments via the sys.argv. This serves two purposes −
#	sys.argv is the list of command-line arguments.
#	len(sys.argv) is the number of command-line arguments.
import sys

# Take the value supplied in argv at index 1 and assume it's a weight parameter.
# argv is an array, which always start from 0, but for argv specifically the 0 index is always the script name.
# e.g. >python.exe .\sal'sshippingproj.py 10

weight = int(sys.argv[1])

#weight = 41.5


#Goal here is to calculate the lowest cost of shipping method for your package, cost determined by weight.
#Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <=6:
    cost_ground = weight * 3.0 + 20
elif weight <=10:
    cost_ground = weight * 4.0 + 20
else:
    weight > 10
    cost_ground = weight * 4.75 + 20
print ("Ground shipping cost is :", cost_ground)

premgroundship = 125.00
print ("Ground Shipping Premium as a reminder is $", premgroundship)


#Drone Shipping
if weight <= 2:
    dcost_ground = weight * 4.5
elif weight <= 6:
    dcost_ground = weight * 9.0
elif weight <=10:
    dcost_ground =weight * 12.0
else:
    weight > 10
    dcost_ground = weight * 14.25
print("Cost for drone shipping is:", dcost_ground)


