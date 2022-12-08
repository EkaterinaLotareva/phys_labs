from saving_to_LaTeX import save_var_latex
import errors
import os

print(os.path.abspath('output_data.csv'))

vars = {}

with open('../data/input_data.txt', 'r') as d:
    for line in d:
        key, value = line.split(' = ')
        vars[key] = list(map(float, value.rstrip().split(', ')))

for a in vars.keys():
    vars[a] = errors.mean(vars[a])
    save_var_latex(str(a), vars[a])

