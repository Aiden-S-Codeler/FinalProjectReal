import random as rand
import csv

def csv_to_dict(path):
    try:
        with open(path, mode = 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            finished = []
            for line in reader:
                i = 0
                current_line = {}
                for column in header:
                    current_line[column] = line[i]
                    if line[i].isdigit(): current_line[column] = int(line[i])
                    i += 1
                finished.append(current_line)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")
    else: return finished
    return []

def save_csv(path, data):
    try:
        if not data: return
        with open(path, mode="w", newline="") as file:
            cleaned_data = []
            for row in data:
                new_row = {}
                for key, value in row.items():
                    if isinstance(value, (list, dict)): new_row[key] = str(value)
                    else: new_row[key] = value
                cleaned_data.append(new_row)
            header = cleaned_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(cleaned_data)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")
