import csv
with open('data_dict.csv', 'w') as file:
    fieldname = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
