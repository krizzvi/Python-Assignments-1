import csv
def read_csv_above_75(filepath):
    high_scorers = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['Marks']) > 75:
                high_scorers.append(row['Name'])
    return high_scorers
