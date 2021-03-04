#FiBONACCi SerIes
import math                                    #importing math library
def check_perfect_square(n):                   #defining a function to check the perfect square of the number
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) ==n:
        return True
    else:
        return False
def isFibonacci(n):                            #defining the Fibonacci function
    res1= 5*n*n+4
    res2= 5*n*n-4
    if check_perfect_square(res1) or check_perfect_square(res2):
        return True

    else:
        return False
num= int(input('Enter the number:'))

if isFibonacci(num):                          #checking the number as Fibonacci or not
    print('Yes, Congratulations. The number is a Fibonacci number.')
else:
    print('No, Sorry. The number is not a Fibonacci number. Try Again!!!')