import os
import csv
from producer_consumer.consumer import output_links

def test_output_links():
    url = 'https://example.com'
    links = ['https://example.com/page1', 'https://example.com/page2']
    output_dir = 'test_output'

    output_links(url, links, output_dir)

    filename = os.path.join(output_dir, f"{url.replace('/', '_').replace(':', '')}_links.csv")
    assert os.path.exists(filename)

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        assert header == ['URL', 'Link']

        expected_rows = [[url, link] for link in links]
        for row, expected_row in zip(csv_reader, expected_rows):
            assert row == expected_row
