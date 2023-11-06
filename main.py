import random
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate a random prime less than 1000
def generate_prime():
    while True:
        prime_candidate = random.randint(2, 999)
        if is_prime(prime_candidate):
            return prime_candidate


# Function to generate psuedorandom list of bits
def generate_bit_string():

    # Generate primes p and q
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    
    # Calculate N and M
    N = p * q
    M = (p - 1) * (q - 1)

    # Generate random e such that gcd(e, M) = 1
    e = random.randint(3, M)
    while math.gcd(e, M) != 1:
        e = random.randint(3, M)

    # Generate random x such that gcd(x, N) = 1
    x = random.randint(2, N)
    while math.gcd(x, N) != 1:
        x = random.randint(2, N)

    # Generate the string of bits
    bit_string = ""
    y = x
    for _ in range(100):
        bi = y % 2
        bit_string += str(bi)
        y = (y ** e) % N

    return bit_string, p, q, e

# Function to call and output psuedorandom bit str to console 
def main():
    bit_str, p, q, e = generate_bit_string()
    print(f"p={p}")
    print(f"q={q}")
    print(f"e={e}")
    print(bit_str)


if __name__ == "__main__":
    main()
