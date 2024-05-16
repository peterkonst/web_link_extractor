import asyncio
import aiohttp
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            logging.info(f"Fetched HTML from {url}")
            return html

async def producer(urls, queue):
    for url in urls:
        html = await fetch_html(url)
        await queue.put((url, html))
        logging.info(f"Added HTML from {url} to queue")


