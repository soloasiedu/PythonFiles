#! python3
import webbrowser

links = ['https://www.google.com', 'https://www.cnn.com', 'https://www.bbc.com']

for i in range(len(links)):
	webbrowser.open_new_tab(links[i])
