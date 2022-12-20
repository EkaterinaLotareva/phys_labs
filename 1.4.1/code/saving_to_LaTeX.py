def save_var_latex(key, value):
    import csv
    import os

    dict_var = {}

    file_path = os.path.join(os.getcwd(), "../data/output_data.csv")

    try:
        with open(file_path, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dict_var[row[0]] = row[1]
    except FileNotFoundError:
        pass

    dict_var[key] = value

    with open(file_path, "w") as f:
        for key in dict_var.keys():
            f.write(f"{key},{dict_var[key]}\n")

