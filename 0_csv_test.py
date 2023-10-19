import csv

def get_rows(filename:str) -> list:
    lretval = []  # result 

    csvfile = open(filename, newline='')
    inreader = csv.reader(csvfile, delimiter=';')
    for row in inreader: 
        lretval.append(row)

    csvfile.close()
    
    return lretval

print(get_rows("iplog.csv")[:5])
