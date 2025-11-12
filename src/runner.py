import json
from src.extractors.linkedin_parser import LinkedInParser
from src.outputs.exporters import Exporter
from src.config.settings import load_settings
from src.config.proxies import load_proxies

def main():
    settings = load_settings()
    proxies = load_proxies()

    parser = LinkedInParser(
        keywords=settings.get("keywords", []),
        location=settings.get("location", None),
        domains=settings.get("domains", []),
        proxies=proxies,
    )

    results = parser.run_search()

    exporter = Exporter(results)
    exporter.to_all()

    print(f"✅ Scraping complete. Extracted {len(results)} profiles.")

if __name__ == "__main__":
    main()