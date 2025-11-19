# 11. Sieve of Eratosthenes Prime Number Generator:

# Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
# Initialize an array of all numbers up to the limit, marking each number as prime initially.
# Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
# The remaining unmarked numbers are the prime numbers within the limit.
# Return the list of prime numbers.

# Function to compute all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(limit: int) -> list[int]:
    # Create a boolean list to track primality of each number (True = prime)
    is_prime: list[bool] = [True] * (limit + 1)
    
    # 0 and 1 are not prime numbers
    is_prime[0:2] = [False, False]

    # Iterate from 2 to the square root of the limit (inclusive)
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:  # If the number is still marked as prime
            # Mark all multiples of i (starting from i*i) as non-prime
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Extract and return all indices that are marked as prime
    primes: list[int] = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Example usage: print all prime numbers up to 50
print(sieve_of_eratosthenes(50))