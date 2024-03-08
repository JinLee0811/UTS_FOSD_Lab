# 1. Enter circle radius: xyz
# 2. Circle area of radius “value of radius go here” is: area
# 3. Sphere volume of radius “value of radius go here” is: volume
# The formula for the volume of a sphere is V = 4/3 π r³, where V = volume and r = radius.
# The area of a circle is pi times the radius squared (A = π r²).


radius = float(input("Enter circle radius: "))
area = 3.14 * radius**2  #
volume = 4 / 3 * 3.14 * radius**3  #


print("Circle of '{0:.2f}'is : '{1:.2f}".format(radius, area))
print("Sphere of '{0:.2f}'is : '{1:.2f}".format(radius, volume))
