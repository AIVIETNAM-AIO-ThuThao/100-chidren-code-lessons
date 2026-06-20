'''Problem 56. Compute the binomial coefficient Cnk or C (n, k) with n and k entered by the user.
The formula for calculating C(n,k) is: C(n,k)= n!/(k!(n - k)!​'''
def factorial(n):
    result = 1
    [result := result * i for i in range(1, n + 1)]    # Using walrus operator (Python 3.8+)
    return result
def binomial_coefficient(k, n):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))


print(binomial_coefficient(2,5))  # test case == C (5, 2) = 10

while True:
    try:
        n, k = map(int, input("Enter 2 positive integers n and k ((k <= n)) to compute the binomial coefficient C(n, k): "))
        if k > n or k*n < 0:
            print("Input does not satisfy the required conditions. Please try again")
            continue
        print(f"The binomial coefficient C (n, k) is {binomial_coefficient(n, k)}")
    except ValueError:
        print("Invalid values. Please try again!")

