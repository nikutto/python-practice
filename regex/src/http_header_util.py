import re

def http_header_mapper(header):
    pattern = r'^ *(?P<key>.*): (?P<value>.*)$'
    regex = re.compile(pattern, re.MULTILINE)

    header_dict = dict()
    for match in regex.finditer(header):
        key = match.group('key')
        value = match.group('value')
        header_dict[key] = value

    return header_dict
