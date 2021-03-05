import sys,webbrowser

try:
    filename=sys.argv[1]
    count=sys.argv[2]
except:
    filename='job.txt'
    count=0
with open(filename) as f:
    content = f.readlines()
if count==0:
    for urls in content:
        webbrowser.open(urls.strip())
else:
    for urls in content[:count]:
        webbrowser.open(urls.strip())



html

<a href=" "