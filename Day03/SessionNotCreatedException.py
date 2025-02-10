import os
import requests
import pandas as pd
from io import StringIO

# URL to scrape
url = 'https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info'

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse tables from the HTML content
tables = pd.read_html(StringIO(response.text))

# Directory to save CSV files
output_dir = r'C:\Users\Dell\Desktop\ApexaiQ\Programs\CSV'
os.makedirs(output_dir, exist_ok=True)

# Save each table as a CSV file
for i, table in enumerate(tables, start=1):
    csv_file = os.path.join(output_dir, f'table_{i}.csv')
    table.to_csv(csv_file, index=False)
    print(f'Saved {csv_file}')
