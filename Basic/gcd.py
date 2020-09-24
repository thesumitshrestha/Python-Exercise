# GCD - Euclid's Algorithm

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
        print(t, a, b)

    return a

print(gcd(8, 20))
