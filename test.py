#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

from random import seed
from random import randint

# brew install wkhtmltopdf
import imgkit


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset:UTF-8" ,
    "Cookie" : "customLocale=zh_TW"
}

def getCharacterPage(name="伊瑞莉雅"):
	
	httpResponse = requests.get("https://tw.op.gg/champion/statistics",headers=headers)
	#textEncoded = httpResponse.text.encode('utf-8')

	regex = r"\""+name+"\" data-champion-key=\"(.*?)\"><a href=\"(.*?)\""
	raw = re.search(regex, httpResponse.text,re.M|re.I)

	return "https://tw.op.gg" + raw.group(2) + "/bot" #by compare

def generateOverviewTable(path):
	httpResponse = requests.get(path,headers=headers)
	regex = r"<table class=\"champion-overview__table champion-overview__table--summonerspell\">(.*?)</table>"
	raw = re.search(regex, httpResponse.text, re.M|re.I|re.S).group(0)

	#replace url
	raw = raw.replace("src=\"//", "src=\"https://", -1)
	return raw


def generateImage(htmlString):
	css = ['./common.css', './champion2.css']
	tmp_filename = 'static/' + str(randint(0, 10))+'.jpg'
	htmlString = """<html lang="zh_TW">
					  <head>
					  	<meta charset="utf-8"/>
					    <meta name="imgkit-format" content="png"/>
					  </head>
					  <body>""" + htmlString + """</body></html>"""
	imgkit.from_string(htmlString, tmp_filename, css=css)
	return tmp_filename

def searchAndGetImage(name="伊瑞莉雅"):
	character_url = getCharacterPage(name)
	character_html = generateOverviewTable(character_url)
	filepath = generateImage(character_html)
	return filepath
