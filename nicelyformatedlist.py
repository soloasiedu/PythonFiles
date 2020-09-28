
def printList(list):
	nicelyFormatedList = ''
	if len(list) < 1:
		return 'Empty string'
	else:
		for i in range(len(list)):
			if i == len(list) - 1:
				nicelyFormatedList += 'and ' + list[i]
			else:
				nicelyFormatedList += list[i] + ', '
	return nicelyFormatedList



spam = ['apples', 'bananas', 'tofu', 'cats']

print(printList(spam))
print(printList([]))
