import requests, bs4, os, sys

#keyword = ' '.join(sys.argv[1:])
keyword = input('Enter the keyword to search') 
url = 'https://imgur.com/search?q=' + keyword
os.makedirs('imgurImages', exist_ok=True) 
print(url)
x = 0
while x < 10:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElem = soup.select('.image-list-link')
    if linkElem == []:
        print('Could not be found')
        x += 1
    else:
        imgUrl = 'https://imgur.com' + linkElem[x].get('href')
        print('Downloading %s '%imgUrl)
        res = requests.get(imgUrl)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        imgSrcs = soup.select('div.Gallery-Content--mediaContainer:nth-child(4) > div:nth-child(1) > div:nth-child(1)')
        print(len(imgSrcs))
        """
        for i in range(len(imgSrcs)):
            imageUrl = imgSrcs[i].get('src')
            print(imageUrl)
            print(os.path.basename(imageUrl))
            imageFile = open(os.path.join('imgurImages', os.path.basename(imageUrl)), 'wb')
            print('Downloading %s '% imageUrl)
            res = requests.get(imageUrl)
            res.raise_for_status()
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        """
        x += 1
          
