import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    t0 = time.time()
    result = gcd(1071, 462)
    print("gcd(1071, 462) =", result)
    print("duration", time.time() - t0)
