import csv


def read_csv(path):
   # Tu código aquí 👇
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total += int(row[1])
   return total
         
response = read_csv('./app/gastos.csv')
print(response)

