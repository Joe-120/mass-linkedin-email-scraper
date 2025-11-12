import time
import random
import requests
from bs4 import BeautifulSoup
from src.extractors.email_utils import extract_email

class LinkedInParser:
    def __init__(self, keywords, location=None, domains=None, proxies=None):
        self.keywords = keywords
        self.location = location
        self.domains = domains or []
        self.session = requests.Session()
        self.proxies = proxies

    def _build_search_url(self, keyword):
        base = "https://www.linkedin.com/search/results/people/"
        params = f"?keywords={keyword}"
        if self.location:
            params += f"&geoUrn={self.location}"
        return base + params

    def _fetch_page(self, url):
        try:
            resp = self.session.get(url, proxies=self.proxies, timeout=10)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(f"⚠️ Failed to fetch {url}: {e}")
            return None

    def _parse_profiles(self, html, keyword):
        soup = BeautifulSoup(html, "html.parser")
        results = []
        profiles = soup.select(".reusable-search__result-container")

        for profile in profiles:
            title = profile.select_one(".entity-result__title-text").get_text(strip=True) if profile.select_one(".entity-result__title-text") else ""
            description = profile.select_one(".entity-result__summary").get_text(strip=True) if profile.select_one(".entity-result__summary") else ""
            url_el = profile.select_one("a.app-aware-link")
            url = url_el["href"] if url_el else ""

            email = extract_email(description, self.domains)
            results.append({
                "keyword": keyword,
                "title": title,
                "description": description,
                "url": url,
                "email": email
            })

        return results

    def run_search(self):
        all_results = []
        for keyword in self.keywords:
            url = self._build_search_url(keyword)
            html = self._fetch_page(url)
            if html:
                parsed = self._parse_profiles(html, keyword)
                all_results.extend(parsed)
                time.sleep(random.uniform(1, 3))
        return all_results