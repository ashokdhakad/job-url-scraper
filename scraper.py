# Importing required modules
import requests
from bs4 import BeautifulSoup



# target websites store in list
site_list = ['https://geeksgod.com/',
             'https://jobsnet.in/',
             'https://www.studentscircles.com/',
             'https://safejob.in/',
             'https://meganaukri.com/',
             'https://aktupapers.in/',
             'https://www.coursejoiner.com/',
             'https://www.yourpedia.in/']

def scrap():
    print ('=================================================')
    print ('               coded by MrPsycho                 ')
    print ('=================================================')
    print ('               ++++++++++++++++++++              ')
    print ('\n                                               ')
    print ('       _,.                                            ')
    print ('     ,` -.)                  ')
    print ('    ( _/-\\-._               ')
    print ('   /,|`--._,-^|            , ')
    print ('   \_| |`-._/||          , | ')
    print ('     |  `-, / |         /  / ')
    print ('     |     || |        /  /  ')
    print ('      `r-._||/   __   /  /   ')
    print ('  __,-<_     )`-/  `./  /    ')
    print ('  \   `---    \   / /  /     ')
    print ('     |           |./  /      ')
    print ('     /           //  /       ')
    print (' \_/  \         |/  /        ')
    print ('  |    |   _,^- /  /         ')
    print ('  |    , ``  (\/  /_         ')
    print ('   \,.->._    \X-=/^         ')
    print ('   (  /   `-._//^`           ')
    print ('    `Y-.____(__}             ')
    print ('     |     {__)              ') 
    print ('           ()                ')

# scrap sites from target sites
def sitescrape(urls):
    print("Scraper is execute ")
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')

    # opening a file in write mode
    f = open("test1.txt", "a")
    # traverse paragraphs from soup
    for link in soup.find_all("a"):
        data = link.get('href')
        if(data == None):
            continue
        else:
            f.write(data)
            f.write("\n")

    f.close()
    
# clear list for new entry
def refresh(site_list):
    f = open('test1.txt', 'r+')
    f.truncate(0)
    for site in site_list:
        sitescrape(site)
    

upperhtml="<!DOCTYPE html>\
<html>\
<head>\
<style>\
body {background-color: black;}\
a {font-size: 20px}\
</style>\
</head>\
<body>\
"

lowerhtml='</body>\
</html>\
'

# open file for divide catergories
file=open('test1.txt','r')


# filter jobes in file
def joblinks(file):
    file.seek(0)
    hire_set=set()
    for line in file:
        if('hiring' in line or 'intern' in line or 'campus-recruitment-drive' in line or 'off-campus' in line or 'recruitment' in line):
            hire_set.add(line)

    #job links store in files
    hire_file=open('job.html','w')
    hire_file.write(upperhtml)
    for link in hire_set:
        a="<a href="+link+' target="_blank">'+link+"</a><br>"
        hire_file.write(a)
        hire_file.write('\n')
    hire_file.write(lowerhtml)
    hire_file.close()
    
#extract courses links in file
def courses(file):
    file.seek(0)
    courses_set=set()
    for line in file:
        if('courses' in line or 'course' in line):
            courses_set.add(line)
    #courses links store in files
    courses_file=open('courses.html','w')
    courses_file.write(upperhtml)
    for link in courses_set:
        a="<a href="+link+' target="_blank">'+link+"</a><br>"
        courses_file.write(a)
        courses_file.write('\n')
    courses_file.write(lowerhtml)
    courses_file.close()
    
def certification(file):
    file.seek(0)
    certificate_set=set()
    for line in file:
        if('certificates' in line or 'certificate' in line or 'scholarship' in line or 'premium' in line or 'preparation-material' in line):
            certificate_set.add(line)
    #courses links store in files
    certificate_file=open('certificate.html','w')
    certificate_file.write(upperhtml)
    for link in certificate_set:
        a="<a href="+link+' target="_blank">'+link+"</a><br>"
        certificate_file.write(a)
        certificate_file.write('\n')
    certificate_file.write(lowerhtml)
    certificate_file.close()
    print("Scraping==Done!")

scrap()
refresh(site_list)
joblinks(file)
courses(file)
certification(file)
