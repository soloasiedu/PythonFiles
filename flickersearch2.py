#! python3
import sys, requests, bs4, webbrowser


textToSearch = ' '.join(sys.argv[1:])
#textToSearch = input('Enter image to search: ')

print(textToSearch)
res = requests.get('https://www.flickr.com/search/?text='+textToSearch)


if res.raise_for_status() == None:
    soupObject = bs4.BeautifulSoup(res.text, 'html.parser')
    searchElems = soupObject.select('.view photo-list-photo-view awake .interaction-view .photo-list-photo-interaction a')
    numSearchesDisplay = min(3, len(searchElems))
    if searchElems == []:
        print('could not be found')
    else:
        for i in range(numSearchesDisplay):
            #print(searchElems[i].get('href'))
            urlToOpen = 'https://www.flickr.com/photos'+ searchElems[i].get('href')
            print('Opening',urlToOpen)
            webbrowser.open(urlToOpen)        
else:
    raise Exception('Connection error')
