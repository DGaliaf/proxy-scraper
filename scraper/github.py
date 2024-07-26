from scraper import Scraper


class GitHubScraper(Scraper):
    """For scraping live proxylist from github"""

    async def handle(self, response):
        tempproxies = response.text.split("\n")
        proxies = set()
        for prxy in tempproxies:
            if self.method in prxy:
                proxies.add(prxy.split("//")[-1])

        return "\n".join(proxies)