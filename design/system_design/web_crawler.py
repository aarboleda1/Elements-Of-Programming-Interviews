"""
Design a Web Crawler: https://www.youtube.com/watch?v=CDXOcvUNBaA

Basic functionality

1) Start with a single URL that contains all the sites we want to crawl
2) For each URL, issue a GET request to fetch the web page content
3) Parse the content and extract the HTML
4) Add new URLS to the pool and keep crawling


Main components

1) HTML Fetcher
    - Retrieves content from a web page
2) Extractor
    - Exracts links from HTML documents
3) Datastore
    - To store retrieved links, metadata
4) Queue
    - To store the list of URLS to download and prioritizie which
        URLS should be downloaded first

class Crawler:
    def __init__(self, data_store, queue):
        self.data_store = data_store
        self.queue = queue
        self.graph = {}

    def crawl_page(self, page):
        await self._enqueue(url)
        while self.queue:
            asyncio.sleep(1)
        if display_results:
            print(graph)
            result = self.graph[page.url]

    def _enqueue(self, url):
        page = Page(url)
        self.graph.add_node(url, page)
        self.

    # Runs in an event loop every 2-3 seconds and polls
    def _crawl():
        while True:
            page = self.data_store.extract_max_priority()

            if not page:
                break

            for neighbor_url in page.neighbor_urls:
                if neighbor_url not in self.seen:
                    self.queue.append(neighbor_url)






"""
