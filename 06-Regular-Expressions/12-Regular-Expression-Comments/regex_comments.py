import re

tag = '<div id="123">Hello</div>'

result = re.match(
    r"""
        <div\s+     # Match opening tag
        id="(\w+)"  # Match id attribute
        >           # End of opening tag
        ([^<>]+)    # Match contents of tag
        </div>      # Closing div tag
    """, 
    tag, re.VERBOSE)

id, content = result.groups()

print(id, content)