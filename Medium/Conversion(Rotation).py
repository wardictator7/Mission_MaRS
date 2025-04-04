import math

def eq(roll, pitch, yaw): # Convert Euler angles (roll, pitch, yaw) in radians to quaternion (w, x, y, z).

    # Angular fns that are used in the conversion
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    # Quaternion components
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    # Rounding the decimals to 4 places
    w = round(w, 4)
    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    return w, x, y, z  # Returning the quaternion values


dr = float(input("Enter the roll value in degrees: "))
dp = float(input("Enter the pitch value in degrees: "))
dy = float(input("Enter the yaw value in degrees: "))

# Converting the roll, pitch, yaw angle from degrees to radians
R = math.radians(dr)
P = math.radians(dp)
Y = math.radians(dy)

quaternion = eq(R, P, Y)
print("Quaternion (w, x, y, z):", quaternion)

# A valid rotation quaternion must have the norm (root( x**2 + y**2 + z**2 + w**2)) as 1