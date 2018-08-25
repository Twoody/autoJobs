from html.parser import HTMLParser  
from urllib.request import urlopen

def getpage(url="", args=None):
	# return html of page if page exists;
	# Else, return empty string;
	# TODO: Error handling if url is incorrect
	# Tanner 20180824
	isquite  = False
	str      = ""
	html     = ""
	response = None
	if args:
		if args['isquite'] and args['isquite'] == True:
			isquite = True
	str += "getpage INIT\n"
	if url == "":
		str += "ERROR: NO url PROVIDED" + "\n"
		if isquite == False:
			print(str)
		return ""
	str += "FINDING CONTENT FOR:\n\t" + url + "\n"
	response = urlopen(url)
	html     = response.read()
	html     = html.decode("utf-8")
	str += html
	if isquite == False:
		print(str)
	return html



if __name__ == "__main__":
	'''
	Tanner 20180824
	Testing the different responses received from different sites.
	Usage:
		python3 getpage.py > out.temp
	'''
	getpage()
	#getpage("https://google.com")
	getpage("http://catalog.registrar.uiowa.edu/")
	#Tri Cities, Washington
	#getpage("https://kpr.craigslist.org/d/software-qa-dba-etc/search/sof")
	getpage("https://orangecounty.craigslist.org/d/software-qa-dba-etc/search/sof")
