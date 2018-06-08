def lagrange_coefficient(t, o, i, x=0):
    num = 1
    den = 1
    for j in range(1, t+1):
        if i != j:
            num = (num * (x - j)) % o
            den = (den * (i - j)) % o
    return (num * den.mod_inverse(o)) % o


def poly_eval(coefficients, x):
    return sum([coefficients[i] * (x ** i) for i in range(len(coefficients))])
