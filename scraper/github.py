from scraper import Scraper


# For scraping live proxylist from github
class GitHubScraper(Scraper):

    async def handle(self, response):
        tempproxies = response.text.split("\n")
        proxies = set()
        for prxy in tempproxies:
            if self.method in prxy:
                proxies.add(prxy.split("//")[-1])

        return "\n".join(proxies)