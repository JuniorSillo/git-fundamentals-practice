import math

# Team Project: Scientific Calculator Application
# Version: 1.2.0

def sin(x):
    """Sine of x"""
    return math.sin(x)

def cos(x):
    """Cosine of x"""
    return math.cos(x)

def log(x):
    """Natural log of x"""
    result = math.log(x)
    print(f"Logging {x}")
    return result

def exp(x):
    """Exponential of x"""
    if x > 100:
        raise ValueError("Exponent too large to compute safely!")
    return math.exp(x)

if __name__ == "__main__":
    print("Scientific Calculator v1.2.0")
    print(f"sin(0) = {sin(0)}")
    print(f"cos(0) = {cos(0)}")
    print(f"log(1) = {log(1)}")
    print(f"exp(0) = {exp(0)}")

