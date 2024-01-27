import urllib.parse
import sys
def format_url(url, params: dict = None) -> str:
    query_str = urllib.parse.urlencode(params)
    return f'{ url }?{ query_str }'


def get_url(keyword):
    params = {
        'wd': str(keyword)
    }
    url = "http://www.baidu.com/s"
    url = format_url(url, params)
    # print(url)

    return url

if __name__ == "__main__":
    for x in sys.stdin:
        print(get_url(x))
