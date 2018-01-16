"""
required module: beautifulsoup4
"""

from urllib import request
from bs4 import BeautifulSoup

def getmeme_jpg():
    """function to get a meme jpg at [here](https://pbs.twimg.com/profile_images/676496806646272000/k2hLF7zz.jpg)

    demonstrating basic request and file writing
    """

    # stock photo meme: https://pbs.twimg.com/profile_images/676496806646272000/k2hLF7zz.jpg

    pic_url = 'https://pbs.twimg.com/profile_images/676496806646272000/k2hLF7zz.jpg' 
    #if "<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] ... " error for HTTPS:
    #go to /Application/Python 3.6/
    #Install Certificates.command
    #credit to: https://stackoverflow.com/questions/42098126/mac-osx-python-ssl-sslerror-ssl-certificate-verify-failed-certificate-verify

    response = request.urlopen(pic_url)

    with open('./meme.jpg', 'wb') as fw:
        fw.write(response.read())


