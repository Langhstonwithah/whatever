# quadratic.py
#A program that computes the real roots of a quadratic equation
#illustrate use of the math library
#Note: This program crashes if the equaion has no real roots

import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a = eval(input("Please enter the coefficents a: "))
    b = eval(input("Please enter the coefficents b: "))
    c = eval(input("Please enter the coefficents c: "))

    discRoot = math.sqrt(b * b - 4 *a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2)

main()