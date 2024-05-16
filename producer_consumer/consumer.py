import logging
from bs4 import BeautifulSoup
import csv
import os

logging.basicConfig(level=logging.INFO)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        url, html = item
        try:
            links = extract_links(html)
            output_links(url, links, output_dir='output')
        except Exception as e:
            logging.error(f"Error processing HTML from {url}: {e}")

def extract_links(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    except Exception as e:
        logging.error(f"Error extracting links: {e}")
        return []

def output_links(url, links, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(output_dir, f"{url.replace('/', '_').replace(':', '')}_links.csv")

    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'Link'])
            for link in links:
                writer.writerow([url, link])
    except Exception as e:
        logging.error(f"Error writing links to file: {e}")




