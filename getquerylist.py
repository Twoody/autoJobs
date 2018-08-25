from getpage import *
import re

def CLResults(html="", args=None):
	'''
	Tanner 20180824
	Purpose:
		Make a list of custom objects via parsing
			craigslist html and query;
		Each result falls between tags:
			<p class="result-info">(.*?)</p>
	'''
	html        = html.replace('\n', ' ')
	html        = html.replace('\r', ' ')
	results     = getresults(html)
	CL_results  = []
	for result in results:
		newobj = {}
		newobj['date']  = parsedate(result)
		newobj['title'] = parsetitle(result)
		newobj['href']  = parsehref(result)
		if validateCLObj(newobj) == True:
			CL_results.append(newobj)
	return CL_results

def validateCLObj(clobj):
	if clobj['date'] == "":
		return False
	if clobj['title'] == "":
		return False
	if clobj['href'] == "":
		return False
	return True
def getresults(html=""):
	'''
	Return list of parsed results from craigslit query
	'''
	CL_resultRE = re.compile(r'<p class="result-info">(.*?)</p>')
	results     = CL_resultRE.split(html)
	return results

def parsedate(html="", args=None):
	"""
	Tanner 20180824
	Find the date in an html string
	"""
	dateRE = re.compile(r'<time .* datetime="(.*?)" .*</time>')
	date   = dateRE.search(html)
	if date:
		date = date.group(1)
		date = date.replace('-', '')
		date = date.replace(':', '')
		date = date.replace(' ', '.')
	else:
		date = ""
	return date

def parsetitle(html=""):
	"""
	Tanner 20180824
	Find the title in an html string
	"""
	titleRE = re.compile(r'<a href=.*?>(.*?)</a>')
	title   = titleRE.search(html)
	if title:
		title = title.group(1)
	else:
		title = ""
	return title

def parsehref(html=""):
	"""
	Tanner 20180824
	Find the href in an html string
	"""
	hrefRE = re.compile(r'<a href="(.*?)".*?>.*?</a>')
	href   = hrefRE.search(html)
	if href:
		href = href.group(1)
	else:
		href = ""
	return href

if __name__ == "__main__":
	'''
	Tanner 20180824
	Testing parsing responses from craigslist.com.
	Usage:
		python3 getquerylist.py > out.temp
	'''
	html = getpage("https://orangecounty.craigslist.org/d/software-qa-dba-etc/search/sof", {'isquite':True})
	results = CLResults(html)
	print("MATCHES: " + str(len(results)) + '\n')
	for obj in results:
		print(obj['date'])
		print(obj['title'])
		print(obj['href'])
		print()

