from HTMLParser import HTMLParser
import urlparse as parse


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        self.daily = False
        self.inA = False
        self.a = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and ('id', 'daily') in attrs:
            self.daily = True
        if tag == 'footer':
            self.daily = False
        if self.daily:
            if tag == 'a':
                if dict(attrs).get('target'):
                    url = parse.urljoin(self.base_url, dict(attrs).get('href'))
                    self.a = url
                    self.inA = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.inA = False

    def handle_data(self, data):
        if self.inA:
            self.links.add((data, self.a))

    def page_links(self):
        return self.links
