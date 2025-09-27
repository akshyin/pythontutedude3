def factorial(n):
    fac=1
    if n<0:
        raise "factorial is not defined for negative numbers";
    if n<2 and n>=0:
        return 1
    for i in range(1,n+1):
        fac=fac*i
    return fac

if __name__ == "__main__":
    n=input("Enter a number: ")
    try:
        n=int(n)
        fac=factorial(n)
        print(f"Factorial of {n} is {fac}");
    except:
        print("factorial can be only for whole number")
