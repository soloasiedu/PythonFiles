import bs4, requests, pyperclip



def getWebsiteSubHeadings(websiteUrl = pyperclip.paste()):
    res = requests.get(websiteUrl)
    listHeaders = []
    if res.raise_for_status() == None:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('html body div.main div h2')
        for i in range(len(elems)):
            listHeaders.append(elems[i].text)
    else:
        raise Exception('Website could not be downloaded')
    return '\n'.join(listHeaders)



userAddress = input('Enter the web address to find website\'s headings or enter \
enter \'no\' if site\'s url is already copied to clipboard: ')

if userAddress == 'no':
    headings = getWebsiteSubHeadings()
    print(headings)
else:
    headings = getWebsiteSubHeadings(userAddress)
    print(headings)



    


