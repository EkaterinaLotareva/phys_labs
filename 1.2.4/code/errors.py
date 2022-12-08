def mean(a):
    return sum(a) / len(a)


def standart_deviation(a):
    return (sum(map(lambda x: (x - mean(x)) ** 2, a)) / (len(a) - 1)) ** 0.5


def full_error(a, system_error):
    return (standart_deviation(a) + system_error)


def relative_error(a, system_error):
    return full_error(a, system_error) / mean(a)
