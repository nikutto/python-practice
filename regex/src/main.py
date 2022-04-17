import re
import pprint
from date_util import date_match
from http_header_util import http_header_mapper

def date_util_demo():
    ymd = date_match("1997/Nov/14")
    print(ymd)

    try:
        ymd = date_match("1997/Nov/14:")
    except ValueError:
        print("OK")
    except:
        raise Exception("This area is not reachable...")

def http_header_util_demo():
    header = """cache-control: max-age=0, private, must-revalidate
    content-encoding: gzip
    content-type: text/html; charset=utf-8
    date: Sun, 17 Apr 2022 05:02:52 GMT
    etag: W/"5b04ec8ee829129dbdc6ff9d757aa552"
    referrer-policy: strict-origin-when-cross-origin
    server: nginx
    strict-transport-security: max-age=2592000
    x-content-type-options: nosniff
    x-download-options: noopen
    x-frame-options: SAMEORIGIN
    x-permitted-cross-domain-policies: none
    x-request-id: 1572c277-6eae-438d-86ea-a4b855bf4bb1
    x-runtime: 0.196395
    x-xss-protection: 1; mode=block
    """
    header_dict = http_header_mapper(header)
    pprint.pprint(header_dict)

def repeat_demo():
    pattern = r'a.+?'
    text = 'abaaaba'
    for match in re.finditer(pattern, text):
        print(match.group())

def main():
    print("# " + date_util_demo.__name__)
    date_util_demo()

    print("# " + http_header_util_demo.__name__)
    http_header_util_demo()

    print("# " + repeat_demo.__name__)
    repeat_demo()
    
if __name__ == '__main__':
    main()
