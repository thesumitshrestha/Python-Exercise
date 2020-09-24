# Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

def result(n1, n2):
    if n1 < 1000 and n2 < 1000:
        results = n1 * n2
        return results

    else:
        results = n1 + n2
        return results


print(result(12, 3))
print(result(1000, 3))
