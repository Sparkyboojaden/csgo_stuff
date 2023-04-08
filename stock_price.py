import requests
from bs4 import BeautifulSoup

# Define the company name and CIK number
company = 'Tractor Supply Company'
cik = '0000916365'

# Define the function to get quarterly sales reports
def get_quarterly_sales_reports(company, cik):
    url = f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-Q&count=100'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr', {'class': 'row'})

    reports = []
    for row in rows:
        cells = row.find_all('td')
        if cells[0].text.strip() == '10-Q':
            date = cells[3].text.strip()
            report_url = 'https://www.sec.gov' + cells[1].find_all('a')[0]['href']
            reports.append((date, report_url))

    return reports

# Call the function to get quarterly sales reports for Tractor Supply Company
reports = get_quarterly_sales_reports(company, cik)
print(reports)

# Print the dates and URLs of the quarterly sales reports
for report in reports:
    print(report[0], report[1])