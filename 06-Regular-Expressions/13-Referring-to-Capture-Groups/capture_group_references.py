import re

tag = '<span id="123">Hello</span>'

result = re.match(
    r"""
        <(\w+)\s+    # Match opening tag
        id="(\w+)"  # Match id attribute
        >           # End of opening tag
        ([^<>]+)    # Match contents of tag
        </\1>       # Closing div tag
    """, 
    tag, re.VERBOSE)

if result is None:
    print("No Match")
else:
    tag, id, content = result.groups()

    print(tag, id, content)