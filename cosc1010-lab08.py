# Steele Jacobson
# UWYO COSC 1010
# Submission Date 11/10/24
# Lab 08
# Lab Section: 12 
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def string_checker(string):
    result = 1
    try:
        float(string)
        result = 0
    except ValueError:
        result = 1
        
    if "." in str(string) and result == 0:
        print("Float")
        return float(string)
    elif result == 0:
        print("Integer")
        return int(string)
    else:
        print("The string is neither an integer nor a float")
        
number = string_checker(input("Enter a string "))
print(number)




print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list



def slope_solver(m,b1,lx,ux):
    y = []
    for i in range (int(lx),int(ux)+1):
        y.append(((i*m)+b1))
    print(y)


inp1 = ""
inp2 = ""
while inp2 != "exit":
    while inp2 != "exit":
        br = 0
        list1 = ["m","b1","lx","ux"]
        list2 = ["","","",""]
        n = 0
        for inp in ["m","b1","lx","ux"]:
            inp1 = input(f"Enter a value for {inp} ")
            list2[n] = inp1
            inp11 = inp1.replace("-","")
            inp12 = inp11.replace(".","")
            if inp12 == "exit":
                print("Function Exited")
                inp2 = "exit"
                br = 1
                break
            elif inp12.isdigit() == False:
                print(f"Invalid Input for {inp}")
                br = 1
                break
            n = n+1
        xb = 0
        if br == 1:
            break
       
    
   
        for inp3 in [list2[2],list2[3]]:
            inp4 = inp3.replace("-","")
            if inp4.isdigit() == False:
                print("Invalid Input for x bounds")
                break
            elif list2[2] > list2[3]:
                xb = 1
                pass
            else:
                pass
        
            if xb == 1:
                print("Lower bound cannot be higher than upper bound")
                break
        if br == 1:
            break
        
        #print(list2)
        try:
            slope_solver(float(list2[0]),float(list2[1]),list2[2],list2[3])
        except:
            print("Input Error")
        else:
            inp2 = "exit"
            break



        #slope_solver(1.1,1.1,1,3)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def quadratic_solver(a,b,c):
    
    fin1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    print(fin1)
    fin2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(fin2)
    
def square_root(d):
    d1 = d.replace(".","")
    if d1.isnumeric() == False:
        print("Null")
        return
    fin3 = (float(d)**0.5)
    print(fin3)

quadratic_solver(int(input("Enter A ")),int(input("Enter B ")),int(input("Enter C ")))
square_root(input("Enter radicand "))