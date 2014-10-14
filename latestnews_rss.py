#!/usr/bin/python

from xml.dom import minidom
import urllib
import time
url='http://www.antaranews.com/rss/nas.xml'
xmldoc = minidom.parse(urllib.urlopen(url))
itemlist = xmldoc.getElementsByTagName('item')
localtime = time.localtime(time.time())
print "=====24 Hours Latest News====="
for s in itemlist:
	post_time = time.strptime(s.childNodes[5].childNodes[0].nodeValue[0:25],"%a, %d %b %Y %H:%M:%S")
	localdate = localtime.tm_mday
	if localdate == post_time.tm_mday:
		if post_time.tm_hour >= 0 and post_time.tm_hour <= localtime.tm_hour:
			print
#			print "kondisi 1-1"			
			print s.childNodes[5].nodeName + " = " + s.childNodes[5].childNodes[0].nodeValue
			print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue			
	elif localdate-1 == post_time.tm_mday:
		if post_time.tm_hour >= localtime.tm_hour and post_time.tm_hour <= 23:
			print		
#			print "kondisi 2-1"	
			print s.childNodes[5].nodeName + " = " + s.childNodes[5].childNodes[0].nodeValue
			print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue			
	
