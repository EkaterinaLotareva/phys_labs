import sympy


def mean(a):
    return sum(a) / len(a)


def standart_deviation(a):
    if len(a) > 1:
        return (sum(map(lambda x: (x - mean(a)) ** 2, a)) / (len(a)-1)) ** 0.5
    else:
        return (sum(map(lambda x: (x - mean(a)) ** 2, a)) / (len(a))) ** 0.5


def full_error(a, system_error):
    return (standart_deviation(a)**2 + system_error**2)**0.5


def relative_error(a, system_error):
    return full_error(a, system_error) / mean(a)

def indirect_error(function, varss, values, errors):
    symb_vars = [0]*len(varss)
    n = [0]*len(varss)
    m = [0]*len(varss)
    for i in range(len(varss)):
        symb_vars[i] = sympy.Symbol(str(varss[i]))
    symb_vars = tuple(symb_vars)
    for i in range(len(varss)):
        n[i] = (sympy.diff(function, varss[i]) * errors[i]) ** 2
        lambd = sympy.lambdify([symb_vars], n[i])
        m[i] = lambd(values)
    return round((sum(m)) ** 0.5, 4)
