import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load URLs from Excel
input_df = pd.read_excel(r'C:\Users\Ankita\OneDrive\Desktop\New folder\Input.xlsx')
urls = input_df['URL'].tolist()  # Ensure 'URL' is the correct column name

print("URLs to process:", urls)  # Debugging: Print URLs

for index, url in enumerate(urls):
    try:
        print("Fetching URL:", url)  # Debugging: Print URL being processed
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debugging: Print HTML structure
        print(soup.prettify())

        # Extract title
        title = soup.find('title').text if soup.find('title') else 'No Title'
        
        # Extract article body from class 'td-post-content tagdiv-type'
        body_div = soup.find('div', class_='td-post-content tagdiv-type')
        body = body_div.get_text() if body_div else 'No Content'
        
        # Save the content to a file
        with open(f'{index}.txt', 'w', encoding='utf-8') as file:
            file.write(title + '\n' + body)
    
    except Exception as e:
        with open(f'{index}_error.txt', 'w', encoding='utf-8') as file:
            file.write(f'Error with URL {url}: {e}')
