import feedparser
url=('https://www.cnnturk.com/feed/rss/dunya/news')
haberler=feedparser.parse(url)
i=0
for x in haberler.entries:
    i+=1
    print(i,".haber")
    print(x.title)
    print(x.link)
    print(x.description)
    print("/n")

