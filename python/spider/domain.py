import urlparse


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        print(str(e))
        return ''


def get_sub_domain_name(url):
    try:
        return urlparse.urlparse(url).netloc
    except Exception as e:
        print(str(e))
        return ''

