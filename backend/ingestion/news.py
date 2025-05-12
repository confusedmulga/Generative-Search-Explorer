import feedparser

def fetch_rss_articles(feed_urls, max_articles=5):
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_articles]:
            articles.append({
                "source": url,
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link
            })
    return articles

if __name__ == "__main__":
    feeds = [
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "http://feeds.bbci.co.uk/news/technology/rss.xml"
    ]
    articles = fetch_rss_articles(feeds)
    for article in articles:
        print(article["title"])
