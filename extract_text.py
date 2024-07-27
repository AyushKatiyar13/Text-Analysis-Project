import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', class_='td-post-content tagdiv-type')
    if content_div:
        return content_div.get_text(strip=True)
    return "Content not found"

def main():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if url:  # Check if URL is not empty
            article_text = extract_article_text(url)
            print(f"Content from {url}:\n{article_text}\n")

if __name__ == "__main__":
    main()
