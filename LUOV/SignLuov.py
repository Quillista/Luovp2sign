import numpy as np
import random
import hashlib

def generate_random_matrix(n, m):
    return np.random.randint(2, size=(n, m))

def generate_polynomial(degree):
    return np.random.randint(2, size=(degree + 1,))

def hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()

def generate_key_LUOV(param_n, param_k, param_m):
    A = generate_random_matrix(param_n, param_m)
    E = generate_random_matrix(param_n, param_k)
    f = generate_polynomial(param_k)
    
    public_key = (A, E)
    secret_key = (E, f)

    return public_key, secret_key

def sign_message(secret_key, message):
    E, f = secret_key
    hashed_message = hash_message(message)
    
    # Create a signature (simplified, usually involves more complex operations)
    # For demonstration, we are just returning a hash and random data
    signature = np.random.randint(2, size=(len(hashed_message),))  # Random binary signature
    return signature

def verify_signature(public_key, message, signature):
    A, E = public_key
    hashed_message = hash_message(message)
    
    # Verification logic (simplified for demonstration)
    # In a real scenario, this would involve more calculations
    return len(signature) == len(hashed_message)  # Dummy check for demonstration

def main():
    # LUOV parameters for different variants
    params = [
        (7, 57, 197),
        (7, 83, 283),
        (7, 110, 374),
    ]
    
    for param_n, param_k, param_m in params:
        public_key, secret_key = generate_key_LUOV(param_n, param_k, param_m)
        
        message = "This is a test message."
        signature = sign_message(secret_key, message)
        
        is_valid = verify_signature(public_key, message, signature)
        
        print(f"Message: {message}")
        print(f"Signature: {signature}")
        print(f"Is the signature valid? {'Yes' if is_valid else 'No'}\n")

if __name__ == "__main__":
    main()
