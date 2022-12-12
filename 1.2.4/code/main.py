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




form_11 = (vars['T1x'] ** 2 + vars['T1y'] ** 2 + vars['T1z'] ** 2) / 3
error_11 = errors.indirect_error('(T1x ** 2 + T1y ** 2 + T1z ** 2) / 3', ('T1x', 'T1y', 'T1x'),
                                 (vars['T1x'], vars['T1y'], vars['T1z']), (full_error['T1x'], full_error['T1y'], full_error['T1z']))

save_var_latex('form11', round(form_11, 3))
save_var_latex('error11', error_11)


form_12 = (vars['T1y']**2 + vars['T2z']**2) / 2
error_12 = errors.indirect_error('(T1y**2 + T1z**2) / 2', ('T1y', 'T1z'), (vars['T1y'], vars['T1z']),
                                 (full_error['T1y'], full_error['T1z']))

save_var_latex('form12', round(form_12, 3))
save_var_latex('error12', error_12)


form_13 = (vars['T1x']**2 + vars['T2z']**2) / 2
error_13 = errors.indirect_error('(T1x**2 + T1z**2) / 2', ('T1x', 'T1z'), (vars['T1x'], vars['T1z']),
                                 (full_error['T1x'], full_error['T1z']))

save_var_latex('form13', round(form_13, 3))
save_var_latex('error13', error_13)


form_14 = (vars['T1y']**2 + vars['T2x']**2) / 2
error_14 = errors.indirect_error('(T1y**2 + T1x**2) / 2', ('T1y', 'T1x'), (vars['T1y'], vars['T1x']),
                                 (full_error['T1y'], full_error['T1x']))

save_var_latex('form14', round(form_14, 3))
save_var_latex('error14', error_14)

print(vars)

form_31 = 1 + (vars['hc']**2 / (3 * vars['rc']**2))
error_31 = errors.indirect_error('1 + hc**2 / (3 * rc**2)', ('hc', 'rc'), (vars['hc'], vars['rc']), (0.005, 0.005))
save_var_latex('form31', round(form_31, 3))
save_var_latex('error31', error_31)

form_32 = vars['T3y'] ** 2 / vars['T3x'] ** 2
error_32 = errors.indirect_error('T3y ** 2 / T3x ** 2', ('T3y', 'T3x'), (vars['T3y'], vars['T3x']), (full_error['T3y'], full_error['T3x']))
save_var_latex('form32', round(form_32, 3))
save_var_latex('error32', error_32)

form_41 = 1 + (vars['hd']**2 / (3 * vars['rd']**2))
error_41 = errors.indirect_error('1 + hd**2 / (3 * rd**2)', ('hd', 'rd'), (vars['hd'], vars['rd']), (0.005, 0.005))
save_var_latex('form41', round(form_41, 3))
save_var_latex('error41', error_41)

form_42 = vars['T4y'] ** 2 / vars['T4x'] ** 2
error_42 = errors.indirect_error('T4y ** 2 / T4x ** 2', ('T4y', 'T4x'), (vars['T4y'], vars['T4x']), (full_error['T4y'], full_error['T4x']))
save_var_latex('form42', round(form_42, 3))
save_var_latex('error42', error_42)



axis_1x = 1 / (vars['T1x']**2 - vars['Tp']**2)**0.5
axis_2x = 1 / (vars['T2x']**2 - vars['Tp']**2)**0.5
axis_2y = 1 / (vars['T2y']**2 - vars['Tp']**2)**0.5
axis_2z = 1 / (vars['T2z']**2 - vars['Tp']**2)**0.5
axis_3x = 1 / (vars['T3x']**2 - vars['Tp']**2)**0.5
axis_3y = 1 / (vars['T3y']**2 - vars['Tp']**2)**0.5
axis_4x = 1 / (vars['T4x']**2 - vars['Tp']**2)**0.5
axis_4y = 1 / (vars['T4y']**2 - vars['Tp']**2)**0.5

save_var_latex('ax1x', round(axis_1x, 3))
save_var_latex('ax2x', round(axis_2x, 3))
save_var_latex('ax2y', round(axis_2y, 3))
save_var_latex('ax2z', round(axis_2z, 3))
save_var_latex('ax3x', round(axis_3x, 3))
save_var_latex('ax3y', round(axis_3y, 3))
save_var_latex('ax4x', round(axis_4x, 3))
save_var_latex('ax4y', round(axis_4y, 3))