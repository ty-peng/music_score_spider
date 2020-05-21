from scrapy import cmdline

cmdline.execute('scrapy crawl tan8 -o score_piano.csv'.split())
# cmdline.execute('scrapy crawl Tan8Spider -o score_piano.json'.split())
