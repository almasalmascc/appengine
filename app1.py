
 # Prime Number Checker
 num = int(input("Enter a number: "))
 factors = []
 
 for i in range(2, num):
     if num % i == 0:
         factors.append(i)
 
 if not factors:
     print(f"{num} is a prime number!")
 else:
     print(f"{num} is not prime. Factors: {factors}")
