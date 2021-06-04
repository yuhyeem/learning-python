weight = 41.5
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


