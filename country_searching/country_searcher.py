import requests
from bs4 import BeautifulSoup

from country_searching.emo_cleaner import EmojiCleaner


class CountryParser:
    def __init__(self):
        self._data = {"Cost of Living": {}}
        self._session = requests.Session()
        self._string_cleaner = EmojiCleaner()

    def search_country(self, country_name: str) -> dict:
        country_url = f'https://livingcost.org/cost/{country_name.lower().strip().replace(" ", "-")}'
        try:
            response = self._session.get(country_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return {}

        soup = BeautifulSoup(response.text, 'lxml')

        for row in soup.find_all('tr'):
            headers = row.find_all('th')
            if len(headers) > 1:
                continue
            raw_category = headers[0].text.strip()
            category = self._string_cleaner.remove_emojis(raw_category)

            if category not in self._data["Cost of Living"]:
                self._data["Cost of Living"][category] = {"One Person": None, "Family of 4": None}

            values = row.find_all('span', {'data-usd': True})
            if len(values) == 2:
                self._data["Cost of Living"][category]["One Person"] = values[0].text
                self._data["Cost of Living"][category]["Family of 4"] = values[1].text
            elif len(values) == 1:
                self._data["Cost of Living"][category]["One Person"] = values[0].text

        return self._data


