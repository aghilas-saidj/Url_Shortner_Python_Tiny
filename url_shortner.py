#=====import_modules======================
import requests , json
import os
from bs4 import BeautifulSoup
import sys

#==========Get_Tiny_Requests========================
url =  raw_input('Enter_The_Url : ')
tiny = "https://tinyurl.com/create.php?source=indexpage&url={}&alias=".format(url)
PARAMS = {'url':url} 
r = requests.get(url = tiny , params = PARAMS)
content_requests = r.content
#os.system("clear")

#===================Open_File_To_Write_The_Requests================
file = open("file.txt" ,  "w")
file.write(content_requests)
file = open("file.txt" , "r")
s = file.read()
file.close()

#=======================Scraping_The_Requests_File_To_Obtain_The_Link=====================
soup = BeautifulSoup(s, "html.parser")
for item in soup.find_all('div',class_=["indent" , ""]):
    file1 = open("file1.txt" , "w")
    file1.write(item.text)
    file1.close()
    grep_link = os.system("grep //tinyurl  file1.txt")
    grep_link_string = str(grep_link)

    file1 = open("file1.txt" , "w")
    file1.write(grep_link_string)
    file1 = open("file1.txt", "r")
    result = file1.read(0)
    file1.close()
    file3 = open("file3.txt" ,  "a")
    file3.write(result)
    file3.close()
    file1.close()
