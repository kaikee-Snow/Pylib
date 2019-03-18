import csv
with open('data.csv', 'w') as cvsfile:
    writer = csv.writer(cvsfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Mike', 20])
    writer.writerow(['1002', 'Bob', 22])
