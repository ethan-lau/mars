import unittest
import urllib2
import sys
import os

sys.path.append('..')
import spider.link_finder
import spider.general


class TestStringMethods(unittest.TestCase):
    def test_urlopen(self):
        url = 'http://toutiao.io'
        req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
        response = urllib2.urlopen(req)
        html_string = response.read()
        finder = spider.link_finder.LinkFinder(url, '')
        finder.feed(html_string)
        finder.close()
        links = finder.page_links()
        i = 0
        if not os.path.exists('file'):
            os.makedirs('file')
        for (key, value) in links:
            try:
                i += 1
                print '{0} {1} {2}'.format(i, key, value)
                req = urllib2.Request(value, headers={'User-Agent': "Magic Browser"})
                response = urllib2.urlopen(req, timeout=5)
                html_s = response.read()
                spider.general.write_file('file/{0}.html'.format(key), html_s)
            except Exception as e:
                print str(e)
