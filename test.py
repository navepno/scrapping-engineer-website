import csv
# запомни
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

#
# def create_csv(filename, data):
#     with open(f'{filename}.csv' 'w', newline='') as csvfile:
#         fieldnames = ['Company', 'Country', 'City', 'Relocation Status',
#                       'Relocation status now', 'Source', 'Last updated']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
