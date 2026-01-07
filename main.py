import math

# Team Project: Scientific Calculator Application
# Version: 1.0.0

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
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    print("Scientific Calculator v1.0.0")
    print(f"sin(0) = {sin(0)}")
    print(f"cos(0) = {cos(0)}")
    print(f"log(1) = {log(1)}")
