##
## Imprima la suma de la segunda columna.
##
data = open("data.csv","r").readline()
[row.split(",") for row in data]
a = 0
[row[1] for row in data]
[a+row for row in data]
a
_grade_.py
