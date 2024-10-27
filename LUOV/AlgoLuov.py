import numpy as np
import random

def generate_random_matrix(n, m):
    return np.random.randint(2, size=(n, m))

def generate_polynomial(degree):
    # Generate a random polynomial of a given degree
    return np.random.randint(2, size=(degree + 1,))

def generate_key_LUOV(param_n, param_k, param_m):
    # Step 1: Generate random matrices A and E
    A = generate_random_matrix(param_n, param_m)
    E = generate_random_matrix(param_n, param_k)

    # Step 2: Generate a random polynomial f
    f = generate_polynomial(param_k)

    # Step 3: Compute the public key
    # Public key is a combination of A, E, and f (in a real scenario)
    # Here we will just return A, E for demonstration
    public_key = (A, E)

    # Secret key is typically (E, f)
    secret_key = (E, f)

    return public_key, secret_key

def main():
    # LUOV parameters for different variants
    params = [
        (7, 57, 197),
        (7, 83, 283),
        (7, 110, 374),
    ]
    
    for param_n, param_k, param_m in params:
        public_key, secret_key = generate_key_LUOV(param_n, param_k, param_m)
        print(f"Public Key for LUOV-{param_n}-{param_k}-{param_m}:")
        print(f"A:\n{public_key[0]}")
        print(f"E:\n{public_key[1]}\n")

        print(f"Secret Key for LUOV-{param_n}-{param_k}-{param_m}:")
        print(f"E:\n{secret_key[0]}")
        print(f"f:\n{secret_key[1]}\n")

if __name__ == "__main__":
    main()
