import math
# TASK 1

try:
    x1 = float(input("Enter first x coordinate: "))
    y1 = float(input("Enter first y coordinate : "))
    x2 = float(input("Enter second x coordinate: "))
    y2 = float(input("Enter second y coordinate: "))
except ValueError:
    print("Please enter a number")
    exit()
total_distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
print("The total distance between two points is ", total_distance)

# task 2
try:
    u = float(input("Enter the intial speed"))
    max_v = float(input("Enter the top speed"))
    a = float(input("Enter the acceleration"))
except ValueError:
    print("Please enter a number")
    exit()
# checking the parameters are positive
if u < 0 or max_v < 0 or a < 0:
    print("Error: Please enter positive  number")
    exit()
#checking the max speed is greater than initial speed
if u > max_v:
    print("Error: Please enter the maximum speed as greater than or equal to initial speed")
    exit()
if a == 0 and u == 0:
    print("Can't move with speed and acceleration is zero")
    exit()
# the total distance
total_distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
final_v = math.sqrt(u*u + 2*a*total_distance)
if final_v > max_v:
    #time took to reach the max speed
    t1 = (max_v - u) / a
    #distance traveled during these time
    s1 = u*t1 + 0.5*a*t1**2
    print("LOG distance", s1)
    # remaining distance
    s2 = total_distance - s1
    # time it took to travel the remaining distance
    t2 = max_v / s2
    # total time
    total_time = t1+t2
else:
    total_time = (final_v - u)/a
print('LOG: max speed: ', max_v, 'final speed: ', final_v)
print("The total time took to travel from point 1 to point 2 is ", total_time)


#task 3


