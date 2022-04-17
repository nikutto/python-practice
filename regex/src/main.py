import re
from date_util import date_match

def date_util_demo():
    ymd = date_match("1997/Nov/14")
    print(ymd)

    try:
        ymd = date_match("1997/Nov/14:")
    except ValueError:
        print("OK")
    except:
        raise Exception("This area is not reachable...")

def main():
    print("# " + date_util_demo.__name__)
    date_util_demo()
    
    
if __name__ == '__main__':
    main()
