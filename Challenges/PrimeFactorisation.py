"""
Challenge: Prime Factor Visualization
Write a Python function named prime_factors_visualization that takes an integer greater than 1 
as input and prints a graphical representation of its prime factors. The function should identify 
the prime factors of the number and display a simple textual visualization of how these factors 
multiply together to form the original number.

Requirements:
Identify Prime Factors: The function should determine the prime factors of the input number.
Visualize Factors: For the visualization:
Each prime factor should be represented by its numeral inside square brackets.
If a prime factor appears multiple times, it should be repeated in the visualization.
The factors should be shown in non-decreasing order.
Example Output:
For the input 360, the prime factorization is 2 x 2 x 2 x 3 x 3 x 5
"""


num = 0

while num == 0:
    num = int(input("Enter a number: "))

def findPrimesBeforeNum(num):
    primesBeforeNum = []

    for i in range(1, num + 1):
        #print(str(num) + " : " + str(i))
        if num % i == 0: #IF A FACTOR
            #print("-    " + str(num) + " : " + str(i))
            for x in range(1, i + 1): # SEARCH THROUGH NUMBERS
                if i % x == 0 and x != 1 and x != i: # TO FIND IF IT'S PRIME
                    break
                elif i % x == 0 and x == i:
                    primesBeforeNum.append(i)
                
                

    return primesBeforeNum

def addPrimesTilNum(num, primes):
    print(primes)

    alteredNum = num
    result = []

    lenPrimes = len(primes) - 1

    for i in range(lenPrimes, -1, -1):
        while True:
            if alteredNum % primes[i] == 0 and primes[i] != 1:
                alteredNum = alteredNum / primes[i]
                result.insert(0, primes[i])
            else:
                break
    
    print(result)

addPrimesTilNum(num, findPrimesBeforeNum(num))