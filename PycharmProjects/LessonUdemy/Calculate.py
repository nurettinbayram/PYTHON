from LessonUdemy.Shapes import sekil

print("Welcome to the tip calculator!")
print(sekil)
total_bil = float(input("What was the total bill? $"))
tip =float( input("How much tip would you like to give? 10, 12, or 15? $"))
people =int( input("How many people to split the bill?"))

result = (total_bil+tip)/people
print("Each person should pay: $", result)
