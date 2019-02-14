# Geometrical parameters in size determination of empirical solder-substrate pairs in microelectronic packaging industries
#https://www.geeksforgeeks.org/python-math-function-sqrt/
#https://www.geeksforgeeks.org/mathematical-functions-in-python-set-3-trigonometric-and-angular-functions/
import math

def calculate_chorddist(myradius,mychord):
    mychorddist = 0.5*math.sqrt(4.0 * myradius ** 2-mychord** 2)
    return mychorddist
def calculate_maskheight(myradius,mychord):
    mymaskheight = myradius-0.5*math.sqrt(4.0 * myradius ** 2-mychord** 2)
    return mymaskheight
sn_size=input("Enter the diameter of solder ball in micrometers:   ")
diameter=sn_size
radius = (diameter/2.0)
mask_size=input("Enter the length of the substrate mask in  micrometers:   ")
chord=mask_size
print("distance from center to substrate (um) is:")
print calculate_chorddist(radius,chord)
print("height/depth of the boundary mask (um) is:")
print calculate_maskheight(radius,chord)
