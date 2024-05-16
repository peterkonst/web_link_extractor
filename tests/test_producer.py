from producer_consumer.producer import producer

def mock_fetch_html(url):
    return "<html><body>Hello, World!</body></html>"


def test_producer_successful(mocker):

    mocker.patch("producer_consumer.producer.fetch_html", side_effect=mock_fetch_html)

    urls = ["https://example.com"]
    queue = []

    producer(urls, queue)

    # Assertions
    assert len(queue) == 1

    item = queue[0]
    assert item[0] == urls[0]
    assert item[1] == mock_fetch_html(urls[0])

