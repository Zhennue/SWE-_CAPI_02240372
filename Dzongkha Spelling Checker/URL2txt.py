import re
import urllib.request

def url_to_text_with_re(url):
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8') 

    plain_text = re.sub(r'<.*?>', '', html_content)  

    plain_text = re.sub(r'\s+', ' ', plain_text).strip()

    return plain_text

url = 'https://csf101-server-cap1.onrender.com/get/input/372'
plain_text = url_to_text_with_re(url)

print(plain_text)

