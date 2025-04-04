# At first the rover has transversed w.r.t the camera's frame of reference....but actually for the task to be complete it must have transversed w.r.t the rover's center frame of reference
# From the given info it can be said that the centre of the  rover is located 55cm behind the camera

# So, I am doing it by taking the markings w.r.t the rover's centre frame of reference

def new_reference_frame (x1,y1,z1):
    xfinal = x1
    yfinal = y1
    zfinal = z1 + 55  # Adjusting frame of reference w.r.t rover's centre
    return xfinal,yfinal,zfinal

def distance (x1,y1,z1): # Distance fn
    return (x1**2 + y1**2 + z1**2)**0.5

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
z = int(input("Enter z coordinate: "))

x_final,y_final,z_final = new_reference_frame(x,y,z)

print("Final coordinates are: ",x_final,y_final,z_final)
print("Distance be4 changing frame of reference is: ",distance(x,y,z))
print("Distance after changing frame of reference is: ",distance(x_final,y_final,z_final))