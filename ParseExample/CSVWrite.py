import csv

def csv_writer(data,path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimeter=",")
        for line in data:
            writer.writeRow(line)

if __name__ == "__main__":
    csv_path = "CSVEx.csv"
