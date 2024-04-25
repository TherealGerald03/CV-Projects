import requests
from bs4 import BeautifulSoup
import csv

url = 'https://coinmarketcap.com/new/'  # paste target url

response = requests.get(url)  # sends requests to the target url

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table rows that contain the cryptocurrencies
    crypto_rows = soup.find_all('tr', {'style': 'cursor:pointer'})

    # This will hold all our scraped data
    cryptocurrencies = []

    for row in crypto_rows:
        # Find the columns in each row
        columns = row.find_all('td')

        # Extract the necessary information from the columns
        try:
            # The structure and indices might change based on the actual page layout
            name_symbol = columns[2].get_text(strip=True)
            price = columns[3].get_text(strip=True)
            change_1h = columns[4].get_text(strip=True)
            change_24h = columns[5].get_text(strip=True)
            market_cap = columns[6].get_text(strip=True)
            volume = columns[7].get_text(strip=True)
            blockchain = columns[8].get_text(strip=True)
            added = columns[9].get_text(strip=True)

            cryptocurrencies.append({
                'Name': name_symbol,
                'Price': price,
                '1h Change': change_1h,
                '24h Change': change_24h,
                'Market Cap': market_cap,
                'Volume': volume,
                'Blockchain': blockchain,
                'Added': added
            })

        except IndexError as e:
            print(f"Error parsing row: {e}")

    # Open the CSV file for writing
    with open('cryptocurrencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', '1h Change', '24h Change', 'Market Cap', 'Volume', 'Blockchain', 'Added']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for crypto in cryptocurrencies:
            writer.writerow(crypto)

    print("Scraping complete and data written to cryptocurrencies.csv")

else:
    print(f"Failed to retrieve web page. Status code: {response.status_code}")
