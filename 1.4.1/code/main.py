from saving_to_LaTeX import save_var_latex
import errors
import math
import os

sigma_a = 0.001
sigma_t = 0.13
n = 20
vars = {}
random_error = {}
full_error = {}
relative_error = {}
sqares = {}
periods = {}

with open('../data/input_data', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))

for a in vars.keys():
    if len(vars[a]) > 1:
         random_error[a] = round(errors.standart_deviation(vars[a]), 3)
         save_var_latex('rde' + str(a), random_error[a])

for a in vars.keys():
    if len(vars[a]) > 1:
        full_error[a] = round(errors.full_error(vars[a], sigma_t), 3)
        save_var_latex('fe' + str(a), full_error[a])

for a in vars.keys():
    if len(vars[a]) > 1:
        relative_error[a] = round(errors.relative_error(vars[a], sigma_t), 3)
        save_var_latex('re' + str(a), relative_error[a])
    else:
        relative_error[a] = round(errors.relative_error(vars[a], sigma_a), 3)
        save_var_latex('re' + str(a), relative_error[a])

for a in vars.keys():
    vars[a] = round(errors.mean(vars[a]), 3)
    save_var_latex(str(a), vars[a])

for a in vars.keys():
    sqares[a] = round(vars[a] ** 2, 3)
    save_var_latex(str(a) + '**2', sqares[a])

for a in vars.keys():
    if a[0] == 't':
        periods['T'+a[1]] = round(vars[a] / 20, 3)
        save_var_latex('T'+a[1], periods['T'+a[1]])

for i in range(1, 9):
    full_error['feT' + str(i)] = full_error['t' + str(i)] / 20
    save_var_latex('feT' + str(i), round(full_error['feT' + str(i)], 3))
    relative_error['reT' + str(i)] = full_error['feT' + str(i)] / periods['T' + str(i)]
    save_var_latex('reT' + str(i), round(relative_error['reT' + str(i)], 3))


def g (Xc, a, T):
    l = 1.002
    Mpr = 0.0770
    Mst = 0.8684
    return(round(((4*math.pi**2)/T**2) * ((l**2/12 + a**2)/(Xc*(1 + Mpr/Mst))), 3))


def g_error (Xc, a, T, error_Xc, error_a, error_T):
    expr = '((4 * 3.14 ** 2) / T ** 2) * ((1.002 ** 2 / 12 + a ** 2) / (Xc * (1 + 0.0770 / 0.8684)))'
    return(errors.indirect_error(expr, ('Xc', 'a', 'T'), (Xc, a, T), (error_Xc, error_a, error_T)))

print(full_error)


for i in range(1, 9):
    vars['g'+str(i)] = g(vars['X' + str(i)], vars['A' + str(i)], periods['T' + str(i)])
    vars['g_error'+ str(i)] = g_error(vars['X' + str(i)], vars['A' + str(i)], periods['T' + str(i)], sigma_a,
      sigma_a, full_error['feT' + str(i)])
    save_var_latex('G'+str(i), vars['g'+str(i)])
    save_var_latex('Ger'+str(i), vars['g_error'+ str(i)])

save_var_latex('Gav', round(sum((9.742, 9.79, 9.738, 9.759, 9.757, 9.832, 9.829, 9.804))/8, 3))
save_var_latex('Gaver', round(sum((0.107, 0.113, 0.102, 0.104, 0.113, 0.111, 0.121, 0.112))/8, 3))


print((0.2678*4*3.14**2)/ (1 + 0.077/0.8684))