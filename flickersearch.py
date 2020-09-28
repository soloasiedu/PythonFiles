#! python3
import sys, requests, bs4, webbrowser


textToSearch = ' '.join(sys.argv[1:])
#textToSearch = input('Enter image to search: ')

print(textToSearch)
res = requests.get('https://imgur.com/search?q='+textToSearch)


if res.raise_for_status() == None:
    soupObject = bs4.BeautifulSoup(res.text, 'html.parser')
    searchElems = soupObject.select('.image-list-link')
    numSearchesDisplay = min(7, len(searchElems))
    for i in range(numSearchesDisplay):
        #print(searchElems[i].get('href'))
        urlToOpen = 'https://imgur.com'+ searchElems[i].get('href')
        webbrowser.open(urlToOpen)
else:
    raise Exception('Connection error')
        
