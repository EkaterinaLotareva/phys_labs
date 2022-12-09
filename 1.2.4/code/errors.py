def mean(a):
    return sum(a) / len(a)


def standart_deviation(a):
    return (sum(map(lambda x: (x - mean(a)) ** 2, a)) / (len(a) - 1)) ** 0.5


def full_error(a, system_error):
    return (standart_deviation(a)**2 + system_error**2)**0.5


def relative_error(a, system_error):
    return full_error(a, system_error) / mean(a)
