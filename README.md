# Proxy scraper

Scrape more than 1K HTTP - HTTPS - SOCKS4 - SOCKS5 proxies in less than 2 seconds.

Scraping fresh public proxies from different sources:

- [sslproxies.org](http://sslproxies.org) (HTTP, HTTPS)
- [free-proxy-list.net](http://free-proxy-list.net) (HTTP, HTTPS)
- [us-proxy.org](http://us-proxy.org) (HTTP, HTTPS)
- [socks-proxy.net](http://socks-proxy.net) (Socks4, Socks5)
- [proxyscrape.com](https://proxyscrape.com) (HTTP, Socks4, Socks5)
- [proxy-list.download](https://www.proxy-list.download) (HTTP, HTTPS, Socks4, Socks5)
- [geonode.com](https://geonode.com) (HTTP, HTTPS, Socks4, Socks5)

## Installation

Use this command to install dependencies.

```bash
pip3 install -r requirements.txt
```

## Usage

For scraping:

```bash
python3 proxyScraper.py -p http
```

- With `-p` or `--proxy`, You can choose your proxy type. Supported proxy types are: **HTTP - HTTPS - Socks (Both 4 and 5) - Socks4 - Socks5**
- With `-o` or `--output`, create and write to a .txt file. (Default is **output.txt**)
- With `-v` or `--verbose`, more details.
- With `-h` or `--help`, Show help to who did't read this README.

## License

[MIT](https://choosealicense.com/licenses/mit/)