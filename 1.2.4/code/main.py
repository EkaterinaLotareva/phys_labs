from saving_to_LaTeX import save_var_latex
import errors
import os



vars = {}
random_error = {}
sys_error_1 = 0.13
sys_error_2 = 0.005
full_error = {}
relative_error = {}
sqares = {}

with open('../data/input_data.txt', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))


for a in vars.keys():
    if len(vars[a]) > 1:
         random_error[a] = round(errors.standart_deviation(vars[a]), 3)
         save_var_latex('rde' + str(a), random_error[a])

for a in vars.keys():
    if len(vars[a]) > 1:
        full_error[a] = round(errors.full_error(vars[a], sys_error_1), 3)
        save_var_latex('fe' + str(a), full_error[a])

for a in vars.keys():
    if len(vars[a]) > 1:
        relative_error[a] = round(errors.relative_error(vars[a], sys_error_1), 4)
        save_var_latex('re' + str(a), relative_error[a])
    else:
        relative_error[a] = round(errors.relative_error(vars[a], sys_error_2), 4)
        save_var_latex('re' + str(a), relative_error[a])

for a in vars.keys():
    vars[a] = round(errors.mean(vars[a]), 3)
    save_var_latex(str(a), vars[a])

for a in vars.keys():
    sqares[a] = round(vars[a] ** 2, 3)
    save_var_latex(str(a) + '**2', sqares[a])


form_21 = (vars['a'] ** 2 * vars['T2x'] ** 2 + vars['b'] ** 2 * vars['T2y'] ** 2 + vars['c'] ** 2 * vars['T2z'] ** 2) / \
          (vars['a'] ** 2 + vars['b'] ** 2 + vars['c'] ** 2)
error_21 = errors.indirect_error('(a ** 2 * T2x ** 2 + b ** 2 * T2y ** 2 + c**2 * T2z**2) / (a **2 + b**2 + c**2)',
                                  ('a', 'T2x', 'b', 'T2y', 'c', 'T2z'),
                                 (vars['a'], vars['T2x'], vars['b'], vars['T2y'], vars['c'], vars['T2z']),
                                 (0.005, 0.133, 0.005, 0.13, 0.005, 0.13))

save_var_latex('form21', round(form_21, 3))
save_var_latex('error21', error_21)


form_22 = (vars['b']**2 * vars['T2y']**2 + vars['c']**2 * vars['T2z']**2) / (vars['c']**2 + vars['b']**2)
error_22 = errors.indirect_error('(b**2 * T2y**2 + c**2 * T2z**2) / (c**2 + b**2)', ('b', 'T2y', 'c', 'T2z'),
                                 (vars['b'], vars['T2y'], vars['c'], vars['T2z']), (0.005, 0.13, 0.005, 0.13))

save_var_latex('form22', round(form_22, 3))
save_var_latex('error22', error_22)


form_23 = (vars['a']**2 * vars['T2x']**2 + vars['c']**2 * vars['T2z']**2) / (vars['c']**2 + vars['a']**2)
error_23 = errors.indirect_error('(a**2 * T2x**2 + c**2 * T2z**2) / (c**2 + a**2)', ('a', 'T2x', 'c', 'T2z'),
                                 (vars['a'], vars['T2x'], vars['c'], vars['T2z']), (0.005, 0.133, 0.005, 0.13))

save_var_latex('form23', round(form_23, 3))
save_var_latex('error23', error_23)


form_24 = (vars['a']**2 * vars['T2x']**2 + vars['b']**2 * vars['T2y']**2) / (vars['b']**2 + vars['a']**2)
error_24 = errors.indirect_error('(a**2 * T2x**2 + b**2 * T2y**2) / (b**2 + a**2)', ('a', 'T2x', 'b', 'T2y'),
                                 (vars['a'], vars['T2x'], vars['b'], vars['T2y']), (0.005, 0.133, 0.005, 0.13))

save_var_latex('form24', round(form_24, 3))
save_var_latex('error24', error_24)



