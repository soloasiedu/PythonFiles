#print('hello')

import requests, bs4, os


url = 'https://xkcd.com'

os.makedirs('comicImages', exist_ok=True)

while url.find('https://xkcd.com/2329/') != 0:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElem = soup.select('#comic img')
    if linkElem == []:
        print('Could not be found')
    else:
        comicUrl = 'https:' + linkElem[0].get('src')
        print('Downloading %s ' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('comicImages', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink = soup.select('a[rel="prev"]')
        url = 'https://xkcd.com'+  prevLink[0].get('href')
print('Done')
        
    
