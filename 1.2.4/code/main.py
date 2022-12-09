from saving_to_LaTeX import save_var_latex
import errors
import os

print(os.path.abspath('output_data.csv'))

vars = {}
random_error = {}
sys_error_1 = 0.13
sys_error_2 = 0.005
full_error = {}
relative_error = {}

with open('../data/input_data.txt', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))

print(vars)

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

