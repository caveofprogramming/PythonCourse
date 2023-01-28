import re

tag = '<div id="123">Hello</div>'

result = re.match(r"<[^>]+>([^<>]+)</[^>]+>", tag)

content = result.group(1)

print(content)