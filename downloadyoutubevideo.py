import youtube_dl, pyperclip, os

os.chdir(r'C:\Users\SOLO\Downloads')
link = [pyperclip.paste()]

ydl_options = {
	'format': 'bestvideo+bestaudio'
	#'writethumbnail': 'writethumbnail',
	#'writesubtitles': 'writesubtitles',
	#'writedescription': 'writedescription'
	}

with youtube_dl.YoutubeDL(ydl_options) as ydl:
	ydl.download(link)
