from getquerylist import *
from getpage import *
import re

def cleanpage(html=""):
	html = html.replace('\n', ' ')
	html = html.replace('\r', ' ')
	html = html.replace('<!DOCTYPE html>', '')
	html = re.sub(r'\s+', ' ', html)
	html = re.sub(r'<!--.*?-->', '', html)
	html = re.sub(r'<script.*?>.*?</script>', '', html)
	html = re.sub(r'<head>.*?</head>', '', html)
	return html

def hasUserBody(html):
	'''
	Tanner 20180824
	Craigslist appears to be storing information in:
		`<section class="userbody">`
	IFF the above exists in the html, return True
	'''
	secRE = re.compile('<section class="userbody">')
	section = secRE.search(html)
	if section:
		return True
	return False
def getuserbody(html):
	'''
	Tanner 20180824
	Craigslist appears to be storing information in:
		`<section class="userbody">`
	Return this segment of html only
	'''
	secRE = re.compile('<section class="userbody">(.*?)</section>')
	section = secRE.search(html)
	if section:
		section = section.group(1)
		section = re.sub('.*</div>', '', section)
	else:
		section = ""
	return section

def findlinks(html):
	#hrefRE = re.compile('<a href="(.*)".*?>(.*)</a>')
	hrefRE = re.compile('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
	hrefs  = hrefRE.findall(html)
	return hrefs

def findemails(html):
	'''
	Return list of emails found in html text;
	TODO: TEST THIS!!!
	'''
	emailRE = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(?:com|org|gov)')
	emails  = emailRE.findall(html)
	return emails
	
def humanreadable(html):
	html = re.sub(r'<br/?>', '\n', html)
	html = re.sub(r'&amp;', '&', html)
	print(html)
	return html

def filterlinks(links):
	'''
	Tanner 20180824
	Go through list of links and remove those that are generic.
	'''
	retlinks = []
	generics = [
		'youtube.com' ,
		'youtu.be' 
	]
	for link in links:
		goodlink = True
		for generic in generics:
			if generic in link:
				goodlink = False
				break
		for currentLink in retlinks:
			#Do not add duplicates
			if currentLink in link:
				goodlink = False
				break
		if goodlink:
			retlinks.append(link)
	return retlinks

def buildCLObj(url):
	html  = getpage(url, {'isquite':True})
	clobj = CLResults(html)
	cnt   = 0;
	cntWithSection = 0
	for obj in clobj:
		date  = obj['date']
		title = obj['title']
		href  = obj['href']
		nextpage   = cleanpage(getpage(href, {'isquite':True}))
		hasSection = hasUserBody(nextpage)
		if hasSection:
			cntWithSection +=1
			userbody    = getuserbody(nextpage)
			foundlinks  = findlinks(userbody)
			foundlinks  = filterlinks(foundlinks)
			foundemails = findemails(userbody)
			for link in foundlinks:
				print(link)
			for email in foundemails:
				print(email)
			clobj[cnt]['linksinpage']  = foundlinks
			clobj[cnt]['emailsinpage'] = foundemails
		cnt += 1
		if cnt > 1:
			break
	print('NUMBER WITH userbody: ' + str(cntWithSection))
	return clobj

if __name__ == "__main__":
	'''
	Tanner 20180824
	Testing retrieving further pages for each href in original query;
	Usage:
		python3 buildCLObj.py > out.temp
	'''
	clobj = buildCLObj("https://orangecounty.craigslist.org/d/software-qa-dba-etc/search/sof")
	
