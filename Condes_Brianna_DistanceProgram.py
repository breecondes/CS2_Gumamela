import math

# Get the x and y coordinates of the first and second points
point_x1 = float(input("Enter the x1: "))
point_x2 = float(input("Enter the x2: "))
point_y1 = float(input("Enter the y1: "))
point_y2 = float(input("Enter the y2: "))

#distance = sqrt(pow(point_x2-point_x1, 2) + pow(point_y2-point_y1, 2)

# Calculate the squared differences between the x-coordinates and y-coordinates
point_a = pow(point_x2-point_x1, 2)
point_b = pow(point_y2-point_y1, 2)

# Add the squared differences together
result = point_a + point_b

# Get the square root of the result to find the distance
distance = math.sqrt(result)

# Display the calculated distance
print("The distance is", distance)
