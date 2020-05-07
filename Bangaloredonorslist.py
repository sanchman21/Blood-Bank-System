import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://www.listofdonors.com/donors-in-bangalore" # this is the url for the site which contains a list of blood donars in bangalore.
html = urllib.request.urlopen(url).read()  # using the urllib commands, we open the url in read form.
soup = BeautifulSoup(html, 'html.parser')  # using the beautiful soup module, we parse the data on the website.

table = soup.table  # we parse the table using soup command.

table_rows = table.find_all('tr')  # we find the tr tags in the table.

lst = []  # empty list.

for tr in table_rows:
    td = tr.find_all('td')  # we find the td tags in the html program for the table.
    row = [i.text for i in td]  # we write the contents of the row in a list named as row.
    lst.append(row)  # we append the row(list) in another list.
lst.pop(0)

print(lst)

bg = input("Enter the type of blood group you want:")
print("These places in bangalore have donors who can donate the", bg, "blood group: ")
for element in lst:
    if bg in element:
        print(element[2])

print("Out of the given places, from which place to you prefer getting the blood?")
place = input()
for element in lst:
    if place in element:
        print("you can contact", element[0], "to get blood from this place.")

print("For more information, click here: http://www.listofdonors.com/donors-in-bangalore")
