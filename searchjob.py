import sys, webbrowser

job = '-'.join(sys.argv[1:len(sys.argv)-1])
location = sys.argv[-1]

print(job)
print(location)

urlToOpen = 'https://www.monster.com/jobs/search/?q='+job.title()+'&where='+location.title()

webbrowser.open(urlToOpen)



               
               
