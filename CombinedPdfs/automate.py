Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:/Users/SOLO/Documents/PythonFiles/emailandphone.py ========
>>> 
========= RESTART: C:/Users/SOLO/Documents/PythonFiles/emailandphone.py ========
>>> import re

stringToSearch = input('Enter a string to check if it is alphanumeric')
alphanumericRegex = re.compile(r'[a-zA-Z0-9]')
mo = alphanumericRegex.search(stringToSearch)
SyntaxError: multiple statements found while compiling a single statement
>>> import re
>>> stringToSearch = input('Enter a string to check if it is alphanumeric')
Enter a string to check if it is alphanumericsetie234sd45
>>> alphanumericRegex = re.compile(r'[a-zA-Z0-9]')
>>> mo = alphanumericRegex.search(stringToSearch)
>>> mo
<re.Match object; span=(0, 1), match='s'>
>>> mo.group()
's'
>>> alphanumericRegex = re.compile(r'[a-zA-Z0-9]+')
>>> mo = alphanumericRegex.search(stringToSearch)
>>> mo
<re.Match object; span=(0, 12), match='setie234sd45'>
>>> mo.group()
'setie234sd45'
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: adhd2452ad452
adhd2452ad452 is alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: hahdadhad
hahdadhad is alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: 13442432
13442432 is alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: 123445
123445 is alphanumeric
>>> adsdd34524
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    adsdd34524
NameError: name 'adsdd34524' is not defined
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: 45666
45666 is alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: @45345
@45345 is alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: @$%^&
@$%^& is not alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: $1234
$1234 is alphanumeric
>>> import re
>>> stringToSearch = input('Enter a string to check if it is alphanumeric: ')
Enter a string to check if it is alphanumeric: @12345
>>> alphanumericRegex = re.compile(r'[a-zA-Z0-9]+')
>>> mo = alphanumericRegex.search(stringToSearch)
>>> mo
<re.Match object; span=(1, 6), match='12345'>
>>> alphanumericRegex = re.compile(r'^[a-zA-Z0-9]$+')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    alphanumericRegex = re.compile(r'^[a-zA-Z0-9]$+')
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\re.py", line 250, in compile
    return _compile(pattern, flags)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\re.py", line 302, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\sre_parse.py", line 668, in _parse
    raise source.error("nothing to repeat",
re.error: nothing to repeat at position 13
>>> alphanumericRegex = re.compile(r'(^[a-zA-Z0-9]$)+')
>>> mo = alphanumericRegex.search(stringToSearch)
>>> mo
>>> mo == None
True
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: @12345
@12345 is not alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: 2234%87ab
2234%87ab is not alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: 12345
12345 is not alphanumeric
>>> 
======== RESTART: C:/Users/SOLO/Documents/PythonFiles/isAlphanumeric.py ========
Enter a string to check if it is alphanumeric: abidjADEd
abidjADEd is not alphanumeric
>>> 
>>> 
>>> 
>>> import re
>>> 
>>> def text_match(text):
	patterns = 'ab*?'
	if re.search(patterns, text):
		return 'Found a match'
	else:
		return 'Not matched!'

	
>>> print(text_match('abc'))
Found a match
>>> print(text_match('abbc'))
Found a match
>>> print(text_match('a'))
Found a match
>>> print(text_match('ac'))
Found a match
>>> 
>>> def text_match1(text):
	patterns = 'ab+?'
	if re.search(patterns, text):
		return 'Found a match'
	else:
		return 'Not matched!'

	
>>> print(text_match1('ab'))
Found a match
>>> print(text_match1('ac'))
Not matched!
>>> 
>>> def text_match0(text):
	patterns = 'ab?'
	if re.search(patterns, text):
		return 'Found a match'
	else:
		return 'Not matched!'

	
>>> print(text_match('abbb'))
Found a match
>>> print(text_match('a'))
Found a match
>>> print(text_match('b'))
Not matched!
>>> print(text_match('ab'))
Found a match
>>> 
>>> 
>>> def text_match3(text):
	patterns = 'ab{3}'
	if re.search(patterns, text):
		return 'Found a match'
	else:
		return 'Not matched!'

	
>>> print(text_match3('ab'))
Not matched!
>>> print(text_match3('abb'))
Not matched!
>>> print(text_match3('abbb'))
Found a match
>>> 
>>> 
>>> def text_match7(text):
	lowerCaseUnderScore = re.compile(r'[a-z]_')
	listOfOccurences = lowerCaseUnderScore.findall(text)
	return listOfOccurences

>>> 
>>> def text_match7(text):
	lowerCaseUnderScore = re.compile(r'([a-z]+)_')
	listOfOccurences = lowerCaseUnderScore.findall(text)
	return listOfOccurences

>>> 
>>> print(text_match7('The boy_ is going_ to the_ black_board to write!'))
['boy', 'going', 'the', 'black']
>>> 
>>> def text_match8(text):
	oneUpperCaseLowercases = re.compile(r'[A-Z][a-z]+')
	listOfOccurences = oneUpperCaseLowercases.findall(text)
	return listOfOccurences

>>> 
>>> print(text_match8('The boy is Going to School on a Bus'))
['The', 'Going', 'School', 'Bus']
>>> 
>>> 
>>> import re
>>> 
>>> 
>>> def matchwordWithOptionalPunctuation(text):
	patterns = '(\w+)(.)?$'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(matchwordWithOptionalPunctuation('The boy.'))
Match found
>>> print(matchwordWithOptionalPunctuation('The boy'))
Match found
>>> 
>>> 
>>> def matchwordWithOptionalPunctuation(text):
	patterns = '\w+\S*$'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(matchwordWithOptionalPunctuation('The boy is goiing!))
				       
SyntaxError: EOL while scanning string literal
>>> print(matchwordWithOptionalPunctuation('The boy is goinging!'))
Match found
>>> print(matchwordWithOptionalPunctuation('The boy is goinging '))
Match not found
>>> print(matchwordWithOptionalPunctuation('The boy is goinging'))
Match found
>>> print(matchwordWithOptionalPunctuation('The boy is goinging      '))
Match not found
>>> print(matchwordWithOptionalPunctuation('The boy is goinging!.?'))
Match found
>>> 
>>> 
>>> def wordContainingz(text):
	patterns = '\w*z\w*'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> 
>>> print(wordContainingz('The boy is a zombie'))
Match found
>>> print(wordContainingz('The boy is a sozombie'))
Match found
>>> print(wordContainingz('The boz is a sombie'))
Match found
>>> print(wordContainingz('The boy is a $zombie'))
Match found
>>> 
>>> 
>>> def wordContainingzNotStartingOrEnding(text):
	patterns = '\w+z\w+'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(wordContainingz('The boy is a $zombie'))
Match found
>>> print(wordContainingzNotStartingOrEnding('The boy is a $zombie'))
Match not found
>>> print(wordContainingzNotStartingOrEnding('The boy is a $ombiez'))
Match not found
>>> print(wordContainingzNotStartingOrEnding('The boy is a $ombzie'))
Match found
>>> print(wordContainingzNotStartingOrEnding('The boy is a zzz'))
Match found
>>> 
>>> 
>>> def wordContainingzNotStartingOrEnding2(text):
	patterns = '\Bz\B'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(wordContainingzNotStartingOrEnding2('The boy is a zzz'))
Match found
>>> 
>>> 
>>> def onlyUpperLowerUnderscore(text):
	patterns = '([a-zA-Z0-9]_)+'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> 
>>> print(onlyUpperLowerUnderscore('This contains ad343AED_ '))
Match found
>>> print(onlyUpperLowerUnderscore('This contains ad343AED '))
Match not found
>>> print(onlyUpperLowerUnderscore('This contains 343AED_ '))
Match found
>>> print(onlyUpperLowerUnderscore('This contains 343_ '))
Match found
>>> 
>>> def onlyUpperLowerUnderscore(text):
	patterns = '[a-zA-Z0-9]+_+'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(onlyUpperLowerUnderscore('This contains 343_ '))
Match found
>>> 
>>> def onlyUpperLowerUnderscore(text):
	patterns = '^[a-zA-Z0-9_]+$'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(onlyUpperLowerUnderscore('This contains 343_ '))
Match not found
>>> 
>>> 
>>> def onlyUpperLowerUnderscoreNS(text):
	patterns = '^[a-zA-Z0-9_]*$'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(onlyUpperLowerUnderscoreNS('This contains 343_ '))
Match not found
>>> print(onlyUpperLowerUnderscore('This contains Python_Exercises_1'))
Match not found
>>> 
>>> print(onlyUpperLowerUnderscore('Python_Exercises_1'))
Match found
>>> 
>>> def onlyUpperLowerUnderscoreNSAnywhere(text):
	patterns = '[a-zA-Z0-9_]*'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Match not found'

	
>>> 
>>> print(onlyUpperLowerUnderscoreNSAnywhere('This contains Python_Exercises_1'))
Match found
>>> 
>>> 
>>> def startStringWithNumber(text):
	# 1dhdsd 1adhd_dhehe
	patterns = '\d[a-zA-Z0-9_]*'
	if re.search(patterns, text):
		return 'Match found'
	else:
		return 'Not found'

	
>>> 
>>> print(startStringWithNumber('The 2eij'))
Match found
>>> print(startStringWithNumber('The 240eij'))
Match found
>>> print(startStringWithNumber('The 29ei_jE'))
Match found
>>> print(startStringWithNumber('The the ieng oeie'))
Not found
>>> 
>>> 
>>> def startwith9(string):
	text = re.compile(r'^5')
	if text.match(string):
		return True
	else:
		return False

	
>>> 
>>> print(startwith9('5eaje'))
True
>>> print(startwith9('5.iehe'))
True
>>> print(startwith9('6-3i4hee'))
False
>>> 
>>> 
>>> ip = '216.008.0000945.0196'
>>> string = re.sub('\.[0]*', '.', ip)
>>> print(string)
216.8.945.196
>>> 
>>> 
>>> def checkNumber9AtStringEnd(text):
	patterns = '\S*5$'
	if re.search(patterns, text):
		return True
	else:
		return False

	
>>> 
>>> print(checkNumber9AtStringEnd('The iehe9'))
False
>>> 
>>> def checkNumber9AtStringEnd(text):
	patterns = '5$'
	if re.search(patterns, text):
		return True
	else:
		return False

	
>>> 
>>> def checkNumber9AtStringEnd(text):
	patterns = '\S*9$'
	if re.search(patterns, text):
		return True
	else:
		return False

	
>>> 
>>> print(checkNumber9AtStringEnd('The iehe9'))
True
>>> print(checkNumber9AtStringEnd('The $52!39de_+9'))
True
>>> print(checkNumber9AtStringEnd('The  9'))
True
>>> 
>>> def checkNumber9AtStringEnd(text):
	patterns = '\S+9$'
	if re.search(patterns, text):
		return True
	else:
		return False

	
>>> 
>>> print(checkNumber9AtStringEnd('The  9'))
False
>>> print(checkNumber9AtStringEnd('The $52!39de_+9'))
True
>>> 
>>> 
>>> 
>>> 
>>> patterns = ['Solomon', 'Asiedu', '0548660348', 'Kwesimintsim']
>>> text = 'My name is Solomon Asiedu and I live in Apremdo'
>>> 
>>> for pattern in patterns:
	print('Searching for "%s" in "%s" ->' % (pattern, text))
	if re.search(pattern, text):
		print('Match found')
	else:
		print('Match not found')

		
Searching for "Solomon" in "My name is Solomon Asiedu and I live in Apremdo" ->
Match found
Searching for "Asiedu" in "My name is Solomon Asiedu and I live in Apremdo" ->
Match found
Searching for "0548660348" in "My name is Solomon Asiedu and I live in Apremdo" ->
Match not found
Searching for "Kwesimintsim" in "My name is Solomon Asiedu and I live in Apremdo" ->
Match not found
>>> 
>>> 
>>> stringToReplaceWhitespaces = 'The boy is going to school'
>>> 
>>> stringToReplaceWhitespaces = re.sub('\s*', '_', stringToReplaceWhitespaces)
>>> print(stringToReplaceWhitespaces)
_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_
>>> stringToReplaceWhitespaces = re.sub('" "+', '_', stringToReplaceWhitespaces)
>>> print(stringToReplaceWhitespaces)
_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_
>>> 
>>> 
>>> stringToReplaceWhitespaces = re.sub('" "', '_', stringToReplaceWhitespaces)
>>> print(stringToReplaceWhitespaces)
_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_
>>> stringToReplaceWhitespaces = re.sub('""', '_', stringToReplaceWhitespaces)
>>> print(stringToReplaceWhitespaces)
_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_
>>> stringToReplaceWhitespaces = stringToReplaceWhitespaces.replace(" ", "_")
>>> print(stringToReplaceWhitespaces)
_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_
>>>  stringToReplaceWhitespaces
 
SyntaxError: unexpected indent
>>> stringToReplaceWhitespaces
'_T_h_e__b_o_y__i_s__g_o_i_n_g__t_o__s_c_h_o_o_l_'
>>> 
>>> 
>>> def extract_date(url):
	# htpps://www.washingtonpost.com/news/football-insider/wp/2016/09/02/o..
	return re.findall(r'/(\d{4})/(\d{2})/(\d{2})/', url)

>>> 
>>> 
>>> url1 = 'htpps://www.washingtonpost.com/news/football-insider/wp/2016/09/02/o'
>>> print(extract_date(url1))
[('2016', '09', '02')]
>>> 
>>> 
>>> dt1 = '1996-04-01'
>>> 
>>> def change_date_format(dt):
	return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1, dt)
		      
SyntaxError: EOL while scanning string literal
>>> def change_date_format(dt):
	return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

>>> 
>>> print('The origial date format is "%s"' % (dt1))
The origial date format is "1996-04-01"
>>> print('The changed date format is "%s"' % (change_date_format(dt1)))
The changed date format is "01-04-1996"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 'c:\\spam\\eggs.png'
'c:\\spam\\eggs.png'
>>> r'c:\spam\eggs.png'
'c:\\spam\\eggs.png'
>>> '\\'.join(['folder1', 'folder2', 'folder3', 'file.png'])
'folder1\\folder2\\folder3\\file.png'
>>> 
>>> 
>>> import os
>>> os.path.join('folder1', 'folder2', 'folder3', 'file.png')
'folder1\\folder2\\folder3\\file.png'
>>> os.sep
'\\'
>>> os.getcwd()
'C:\\Users\\SOLO\\Documents\\PythonFiles'
>>> .\
   
SyntaxError: invalid syntax
>>> os.path.abspath('hello.py')
'C:\\Users\\SOLO\\Documents\\PythonFiles\\hello.py'
>>> 
>>> 
>>> os.makedirs('c:\\users\\solo\\documents\\delicious\\food\\drinks')
>>> 
>>> helloFile = open('c:\\users\solo\\documents\\hello.txt')
Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    helloFile = open('c:\\users\solo\\documents\\hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\solo\\documents\\hello.txt'
>>> helloFile = open('c:\\users\solo\\documents\\pythonfiles\\hello.txt')
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    helloFile = open('c:\\users\solo\\documents\\pythonfiles\\hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\solo\\documents\\pythonfiles\\hello.txt'
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\SOLO\\Documents\\PythonFiles\\hello.txt'
>>> import os
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.py')
>>> helloFile.read()
"# This program says hello and asks for your name\nprint('Hello world!')\nprint('What is your name?')\nname = input()\nprint('It is good to meet you ' + name)\nprint('The length of your name is:')\nprint(len(name))\nprint('What is your age?')\nage = input()\nprint('You will be ' + str(int(age) + 5) + ' in 5 years time')\n"
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
>>> helloFile.read()
'Hello World!'
>>> helloFile.close()
>>> helloFile.read()
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    helloFile.read()
ValueError: I/O operation on closed file.
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
>>> helloFile.read()
'Hello World!'
>>> content = helloFile.read()
>>> print(content)

>>> print(content)

>>> content
''
>>> helloFile.readlines()
[]
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
>>> helloFile.read()
'Hello World!'
>>> content = helloFile.read()
>>> content
''
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
>>> content = helloFile.read()
>>> content
'Hello World!'
>>> linebyline = helloFile.readlines()
>>> linebyline
[]
>>> helloFile = open(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt')
>>> linebyline = helloFile.readlines()
>>> linebyline
['Hello World!']
>>> helloFile.close()
>>> linebyline
['Hello World!']
>>> 
>>> anotherFileObject = open(r'C:\Users\SOLO\Documents\PythonFiles\hello2.txt', 'w')
>>> anotherFileObject.write('Hello world!\nWelcome to the exciting world of programming')
57
>>> anotherFileObject.close()
>>> import os
>>> os.getcwd()
'C:\\Users\\SOLO\\Documents\\PythonFiles'
>>> print(os.getcwd())
C:\Users\SOLO\Documents\PythonFiles
>>> 
>>> bacon = open('hello2.txt', 'a')
>>> bacon.write('\nYou are a super human being now!!!')
35
>>> bacon.close()
>>> 
>>> 
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats'] = ['Zophie', 'Simon', 'Pooka', 'Fat-tail', 'Cleo']
>>> shelfFile.close()
>>> 
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats']
['Zophie', 'Simon', 'Pooka', 'Fat-tail', 'Cleo']
>>> shelfFile.close()
>>> 
>>> shelfFile = shelve.open('mydata')
>>> shelfFile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x0335DA78>)
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Simon', 'Pooka', 'Fat-tail', 'Cleo']]
>>> shelfFile.close()
>>> 
>>> 

>>> 

>>> 

>>> 
>>> import shutil
>>> shutil.copy(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt', r'C:\Users\SOLO\Documents\delicious')
'C:\\Users\\SOLO\\Documents\\delicious\\hello.txt'
>>> shutil.copy(r'C:\Users\SOLO\Documents\PythonFiles\hello.txt', r'C:\Users\SOLO\Documents\delicious\hellocopied.txt')
'C:\\Users\\SOLO\\Documents\\delicious\\hellocopied.txt'
>>> shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food\drinks', r'C:\Users\SOLO\Documents\delicious\food')
Traceback (most recent call last):
  File "<pyshell#376>", line 1, in <module>
    shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food\drinks', r'C:\Users\SOLO\Documents\delicious\food')
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 548, in copytree
    return _copytree(entries=entries, src=src, dst=dst, symlinks=symlinks,
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 449, in _copytree
    os.makedirs(dst, exist_ok=dirs_exist_ok)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\os.py", line 221, in makedirs
    mkdir(name, mode)
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\SOLO\\Documents\\delicious\\food'
>>> shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food\drinks', r'C:\Users\SOLO\Documents\delicious')
Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food\drinks', r'C:\Users\SOLO\Documents\delicious')
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 548, in copytree
    return _copytree(entries=entries, src=src, dst=dst, symlinks=symlinks,
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 449, in _copytree
    os.makedirs(dst, exist_ok=dirs_exist_ok)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\os.py", line 221, in makedirs
    mkdir(name, mode)
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\SOLO\\Documents\\delicious'
>>> shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food', r'C:\Users\SOLO\Documents\delicious\food\drinks')
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food', r'C:\Users\SOLO\Documents\delicious\food\drinks')
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 548, in copytree
    return _copytree(entries=entries, src=src, dst=dst, symlinks=symlinks,
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\shutil.py", line 449, in _copytree
    os.makedirs(dst, exist_ok=dirs_exist_ok)
  File "C:\Users\SOLO\AppData\Local\Programs\Python\Python38-32\lib\os.py", line 221, in makedirs
    mkdir(name, mode)
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\SOLO\\Documents\\delicious\\food\\drinks'
>>> shutil.copytree(r'C:\Users\SOLO\Documents\delicious\food', r'C:\Users\SOLO\Documents\delicious\food\food_backup')
'C:\\Users\\SOLO\\Documents\\delicious\\food\\food_backup'
>>> 