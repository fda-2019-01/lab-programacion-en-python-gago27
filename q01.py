##
## Imprima la suma de la segunda columna.
##
data = open("lab-programacion-en-python-gago27/data.csv","r").readline()
[row.split(",") for row in data]
a = 0
[row[1] for row in data]
for row in data:
  a= a+ int(row)
print(a)
__grade__.py
