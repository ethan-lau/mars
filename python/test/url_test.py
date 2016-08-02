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
        links = finder.page_links()
        i = 0
        if not os.path.exists('file'):
            os.makedirs('file')
        for link in links:
            try:
                req = urllib2.Request(link, headers={'User-Agent': "Magic Browser"})
                response = urllib2.urlopen(req)
                html_s = response.read()
                print '{0} {1}'.format(i, link)
                spider.general.write_file('file/{0}.html'.format(i), str(html_s))
                i += 1
            except Exception as e:
                print str(e)



