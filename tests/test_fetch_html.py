import asyncio
import aiohttp
import logging
import pytest
from producer_consumer.producer import fetch_html

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_fetch_html_successful(event_loop, mocker):
    mock_session = mocker.MagicMock()
    mock_response = mocker.MagicMock()
    mock_response.text.return_value = "<html><body>Hello, World!</body></html>"
    mock_session.get.return_value.__aenter__.return_value = mock_response

    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    url = "https://example.com"
    html = await fetch_html(url)

    assert html == "<html><body>Hello, World!</body></html>"
    mock_session.get.assert_called_once_with(url)
