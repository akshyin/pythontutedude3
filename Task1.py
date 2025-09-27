def factorial(n):
    #intailising final value with 1 as factorial is found using multiplication and it should start with 1
    fac=1
    #if n is negative, as mathematical function it should return that factorial is not defined for negative number
    if n<0:
        raise "factorial is not defined for negative numbers";
    # if n is 0 or 1, value of factorial would be 1
    if n<2 and n>=0:
        return fac
    #if n>=2 then factorial(n)=factorial(n-1)*n so expansion of the for loop would be fac=1*2*3 for n 3
    for i in range(1,n+1):
        fac=fac*i
    return fac

if __name__ == "__main__":
    #Asks user for the input the number
    n=input("Enter a number: ")
    try:
        #user may accidently use a value with is not convertable to integer
        n=int(n)
        #factorial function will take care if n is passed as whole number or not as it would give error
        # and error will not execute next line but go to except section and would print error statement provided
        fac=factorial(n)
        print(f"Factorial of {n} is {fac}");
    except:
        #in case of any error, as we know factorial is valid for whole number so any error would lead to this statement
        print("factorial can be only for whole number")
