print("Welcome to CS 121: Advanced Computer Programming!")
name = input("Enter your name: ")
print("This course will be fun, " +name+ "!" )


#exercise 2
for x in range(7, 42, 7):
    if x % 2 == 0:
        print("\t", x)
    else: print(x) 

#exercise 3
#formula (0°C × 9/5) + 32 

cel = input("Enter a Celsius value: ")
formula = float(cel) * 9/5+32
print( cel + " Celsius is ", formula, " Fahrenheit" )
