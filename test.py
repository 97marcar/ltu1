import csv
lista = [["abc","123","hehe"]]

with open("test.csv","wb") as csvfile:
    write = csv.writer(csvfile, delimiter=';')
    for n in range(len(lista)):
        write.writerow(lista[n])

lista = ["aaa"]
with open('test.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        lista.append(row)

print lista
