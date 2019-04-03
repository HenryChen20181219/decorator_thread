import re

s = '<a href=http://www.mianwww.com/html/category/it-interview/flex>Flex</a>'
href = re.search(r'href=(.*?)>',s)
print(href.group(1))


