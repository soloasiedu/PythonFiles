import re


message = 'Call me on 223-465-7890 landline or 355-567-5643 office number or 486-789-1111 \
home number'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

ao = phoneNumRegex.findall(message)
print(ao)
