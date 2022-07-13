urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(https?://)(www\.)?(\w+)(\.\w+)')
sub_url = pattern.sub(r'\3\4', urls)
print(sub_url)

'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')
matches = pattern.findier(emails)

for items in matches:
    print(items)
'''