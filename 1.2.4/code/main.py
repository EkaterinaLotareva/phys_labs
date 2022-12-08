from saving_to_LaTeX import save_var_latex
import errors
import os

print(os.path.abspath('output_data.csv'))

vars = {}

with open('../data/input_data.txt', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))

av = errors.mean(vars['a'])

print(av)

save_var_latex('average', av)

