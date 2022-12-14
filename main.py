import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import re

# aria-label="Turkey Flag"
filename = 'Turkey'
url = requests.get('https://engineer-petr.github.io/')

soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find_all('table')[1]
table_body = table.find('tbody')
rows = table_body.find_all('tr')

fieldnames = ['Company', 'Company Link', 'Country', 'City', 'Relocation Status',
              'Relocation status now', 'Source', 'Source Link', 'Last updated']

with open(f'{filename}.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        data = {
            'Company': '',
            'Company Link': '',
            'Country': '',
            'City': '',
            'Relocation Status': '',
            'Relocation status now': '',
            'Source': '',
            'Source Link': '',
            'Last updated': '',
        }
        col = row.find_all('td')[1]
        # print(row, end='\n\n\n\n')
        elem = col.find('i', attrs={'aria-label': f'{filename} Flag'})
        if elem is not None:


            # company name and link
            if row.find('td').find('a') is not None:
                company_link = row.find('td').find('a')['href']
                company = row.find('td').find('a').contents[0]
                data['Company'] = company
                data['Company Link'] = company_link
                # print(company)
            else:
                company = row.find('td').contents[0]
                data['Company'] = company
                data['Company Link'] = ''

            # country name
            country_field = row.find_all('i')
            for i in country_field:
                country = i['aria-label'].split()[0]
                data['Country'] += country + ', '

            # cities
            cities = row.find_all('td')[2].contents[0]
            data['City'] = cities

            # relocation status
            relocation_status = row.find_all('td')[3].contents[0]
            data['Relocation Status'] = relocation_status

            # relocation status now
            relocation_status_now = row.find_all('td')[4].contents[0]
            data['Relocation status now'] = relocation_status_now

            # source
            source = row.find_all('td')[5].contents[0]
            data['Source'] = source

            # last updated
            last_updated = row.find_all('td')[6].contents[0]
            data['Last updated'] = last_updated

            writer.writerow(data)
            # print(data)

print('done')


