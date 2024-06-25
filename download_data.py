import requests
from bs4 import BeautifulSoup
import zipfile
import io
import pandas as pd

button_path = "a"

url = "https://i2ds.org/datos-abiertos/"

file_path = "./accident_data"

# Download the webpage
response = requests.get(url)

# Parse the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links on the webpage
links = soup.find_all(button_path)

for link in links:
    # Check if the link is to a ZIP file
    if 'zip' in link['href']:
        # Download the ZIP file
        zip_response = requests.get(link['href'])
        z = zipfile.ZipFile(io.BytesIO(zip_response.content))
        
        # Extract all the files from the ZIP file
        z.extractall(path = file_path)