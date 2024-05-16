import asyncio
import logging
import os
import csv
import pytest
from producer_consumer.consumer import consumer

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def test_data(tmpdir):
    output_dir = tmpdir.mkdir("test_output")

    queue = asyncio.Queue()
    queue.put_nowait(('https://example.com', '<a href="https://example.com/page1">Link 1</a>'))

    return queue, output_dir

@pytest.mark.asyncio
async def test_consumer(test_data):

    queue, output_dir = test_data

    await consumer(queue, output_dir=output_dir)

    filename = os.path.join(output_dir, 'example.com_links.csv')
    assert os.path.exists(filename)

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        assert header == ['URL', 'Link'] 

        expected_row = ['https://example.com', 'https://example.com/page1']
        row = next(csv_reader)
        assert row == expected_row 

