from HTMLParser import HTMLParser
import urlparse as parse


class LinkFinder(HTMLParser):
    daily = False

    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and ('id', 'daily') in attrs:
            self.daily = True
        if tag == 'footer':
            self.daily = False
        if self.daily:
            if tag == 'a':
                for (attribute, value) in attrs:
                    if attribute == 'href':
                        url = parse.urljoin(self.base_url, value)
                        self.links.add(url)

    def page_links(self):
        return self.links


class RedirectFinder(HTMLParser):
    redirect = ''

    def handle_startendtag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    self.redirect = value


