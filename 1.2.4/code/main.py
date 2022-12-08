from saving_to_LaTeX import save_var_latex
import errors
import os

print(os.path.abspath('output_data.csv'))

vars = {}
random_error = {}

with open('../data/input_data.txt', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))

for i in vars.keys():
    if len(vars[i]) > 1:
         random_error[i] = errors.standart_deviation(vars[i])
         save_var_latex('random_error_' + str(i), random_error[i])

for a in vars.keys():
    vars[a] = round(errors.mean(vars[a]), 3)
    save_var_latex(str(a), vars[a])

