import math


if __name__ == "__main__":
    n=input("Enter a number ")
    try:
        n=float(n)
        if n>=0:
            print(f"square root: {math.sqrt(n)}")
        else:
            print(f"square root is not defined for {n}")
        if n>0:
            print(f"Logarithm: {math.log(n,math.e)}")
        else:
            print(f"Logarithm is not defined for negative numbers or zero")
        print(f"Sine: {math.sin(n)}")
    except:
        print("mathematical function can be executed for integer or floating point numbers only")
