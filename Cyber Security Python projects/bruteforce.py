import hashlib
import itertools
import string
import time

TARGET_HASH = hashlib.sha256("test".encode()).hexdigest()

def brute_force(max_length=4):
    chars = string.ascii_lowercase
    start = time.time()

    print("Starting brute force simulation...")
    for length in range(1, max_length + 1):
        print(f"Trying length: {length}")

        for combo in itertools.product(chars, repeat=length):
            attempt = "".join(combo)

            if hashlib.sha256(attempt.encode()).hexdigest() == TARGET_HASH:
                print("\nPassword FOUND!")
                print("Password:", attempt)
                print("Time taken:", time.time() - start, "seconds")
                return

            print("Trying:", attempt, end="\r")

    print("\nPassword NOT found.")
    print("Time taken:", time.time() - start, "seconds")

if __name__ == "__main__":
    brute_force(4)
