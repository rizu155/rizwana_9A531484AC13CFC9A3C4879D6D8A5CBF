def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
      
     
  
number = int(input("Enter a Number: "))
res=factorial(number)

print("Factorial of {} is {}".format(number,res))