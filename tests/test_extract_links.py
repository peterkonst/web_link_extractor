from producer_consumer.consumer import extract_links

def test_extract_links_with_links():
    html = '<a href="https://example.com">Link 1</a><a href="https://example.com/page2">Link 2</a>'
    expected_links = ['https://example.com', 'https://example.com/page2']
    assert extract_links(html) == expected_links

def test_extract_links_without_links():
    html = '<p>No links here</p>'
    expected_links = []
    assert extract_links(html) == expected_links

def test_extract_links_with_invalid_html():
    html = 'Invalid HTML'
    assert extract_links(html) == []