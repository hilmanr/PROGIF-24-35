#!/usr/bin/python

from xml.dom import minidom
import urllib
import time
url='http://www.antaranews.com/rss/nas.xml'
xmldoc = minidom.parse(urllib.urlopen(url))
itemlist = xmldoc.getElementsByTagName('item')
localtime = time.localtime(time.time())
print "\n=====24 Hours Latest News====="
print "by: Hilman Ramadhan-18212024 and Ghani Ruhman-18212035"
localtime_sum = time.mktime(localtime)
for s in itemlist:
	post_time = time.strptime(s.childNodes[5].childNodes[0].nodeValue[0:25],"%a, %d %b %Y %H:%M:%S")
	post_time_sum = time.mktime(post_time)
	if localtime_sum - post_time_sum <= 86400:
		print	
		print s.childNodes[5].nodeName + " = " + s.childNodes[5].childNodes[0].nodeValue
		print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue
		print s.childNodes[3].nodeName + " = " + s.childNodes[3].childNodes[0].nodeValue
print

		
