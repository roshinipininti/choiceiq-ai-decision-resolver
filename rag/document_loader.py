import requests
from bs4 import BeautifulSoup


def load_document(url: str) -> str:
    """
    Downloads a webpage and extracts readable text.
    """

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "lxml")

        # remove unnecessary tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")

        text = " ".join(text.split())

        return text

    except Exception:
        return ""