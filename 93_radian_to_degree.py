'''
Create a function that takes an angle in radians and returns the corresponding angle
in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8
'''
import math
def radian_to_degree(radian):
    degree = radian * (180/math.pi)
    
    return degree

print("Radians to Degreee : ", radian_to_degree(1))
print("Radians to Degreee : ", radian_to_degree(20))
print("Radians to Degreee : ", radian_to_degree(50))