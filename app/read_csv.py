from collections.abc import Iterable
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      Iterable = zip(header, row)  # une el encabezado con cada array para crear tuplas
      country_dict = {key: value for key, value in Iterable}
      data.append(country_dict) # agrega cada tupla a la lista
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
  