#! python3
import requests, bs4, sys, webbrowser


keywordToSearch = ' '.join(sys.argv[1:])
print(keywordToSearch)


res = requests.get('https://www.google.com/search?client=firefox-b-d&q='+keywordToSearch)

if res.raise_for_status() == None:
    soupObject = bs4.BeautifulSoup(res.text, 'html.parser')
    searchElems = soupObject.select('.iUh30 bc tjvcx')
    numOpen = min(5, len(searchElems))
    for i in range(numOpen):
        print(searchElems[i].getText())
        #urlToOpen = 'https//:'+ searchElems[i].getText()
        #print('Opening', urlToOpen)
        #webbrowser.open_new_tab(urlToOpen)
else:
    raise Exception('Page could not be downloaded')
