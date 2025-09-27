import math


if __name__ == "__main__":
    #takes input from user
    n=input("Enter a number ")
    try:
        #try to convert it in float, as integer input for given  mathematical operation, float is appropriate
        n=float(n)
        #As we know, square root can be for only non-negative numbers
        if n>=0:
            print(f"square root: {math.sqrt(n)}")
        
        else:
            #incase of n is given negative
            print(f"square root is not defined for {n}")
        #As log domain is only non zero  positive number
        if n>0:
            print(f"Logarithm: {math.log(n,math.e)}")
        else:
            print(f"Logarithm is not defined for negative numbers or zero")
        #prints the value of sin, n is treated as given in radian
        print(f"Sine: {math.sin(n)}")
    except:
        #Any error should provide the reason of error, error may be appropriatly provided in this context. 
        print("mathematical function can be executed for integer or floating point numbers only")
