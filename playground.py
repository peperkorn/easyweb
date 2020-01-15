a = "https://www.website.ch/weiterertext"
b = "www.website.de"
c = "shop.website.ch"
d = "http://www.website.ch/weiterertext"
e = "http://www.website.ch/weiterertext/bla/bla/bla/bla"
f = "website.ch"
set = (a, b, c, d, e, f)

filewrite = open("websiteaufbereitung_similarweb.txt", "w")
for i in range(len(set)):
	short = set[i].replace("www.","").replace("https://","").replace("http://","").replace("shop.","").split("/") # Die Aufzählung kann durch alles, was "links" steht und weg soll ergänzt werden.
	del short[1:100]
	print(short)
	for j in range(len(short)):
		filewrite.write('"' + short[j] + '"' + " , ")
filewrite.close()