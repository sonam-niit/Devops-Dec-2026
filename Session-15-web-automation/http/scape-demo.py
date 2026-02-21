# pipenv install beautifulsoup4

from bs4 import BeautifulSoup

html="""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<h1 class="info">My Second Heading</h1>
<p>My first paragraph.</p>

</body>
</html>"""

# Parse String in html

soup=BeautifulSoup(html,"html.parser")
print("Title: ",soup.title.text)
print("Heading: ",soup.h1.text) # get first h1 tag
print("Heading: ",soup.find("h1",class_="info").text) # this will find based on the class
print("Paragraph: ",soup.p.text)