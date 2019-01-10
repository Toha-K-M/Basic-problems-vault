import random
import urllib.request #enable us to get data from website

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://pmctvline2.files.wordpress.com/2016/05/person-of-interest-root-dies-amy-acker.jpg?w=621")

