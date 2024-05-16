import asyncio
from producer import producer
from consumer import consumer
import logging

logging.basicConfig(level=logging.INFO)

async def main():
    try:
        urls = ['https://www.youtube.com/', 'https://www.google.com/maps']

        queue = asyncio.Queue()

        producer_task = asyncio.create_task(producer(urls, queue))
        consumer_task = asyncio.create_task(consumer(queue))

        await producer_task
        await queue.put(None)
        await consumer_task
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    asyncio.run(main())
