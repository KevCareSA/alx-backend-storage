# test_web.py

from web import get_page  # Updated import statement

url_to_fetch = "http://slowwly.robertomurray.co.uk/delay/10000/url/http://www.google.com"
html_content = get_page(url_to_fetch)

if html_content:
    print("\nHTML Content (Decorated Function):")
    print(html_content)
