#!/usr/bin/env python

"""

Python script to extract all of the transcripts from the Spongebob fandom website.

"""

from bs4 import BeautifulSoup
import urllib
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Set up the web browser
options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('https://spongebob.fandom.com/wiki/List_of_transcripts')
html_page = driver.page_source
soup = BeautifulSoup(html_page, features="lxml")

linksList = []
transcriptLinks = []

#Get all transcript links from the page
for link in soup(href = True):
	linksList.append(link.get('href'))

for link in linksList:
	if "transcript" in link and not("transcripts" in link):
		transcriptLinks.append(link)
print (transcriptLinks)


#Extract speech transcript portion from each transcript link and compile into a txt file
separator = "--------------------\n"
with open('compiled_transcripts.txt', 'w') as f:
	for transcriptURL in transcriptLinks:
		url = "https://spongebob.fandom.com" + transcriptURL
		episode_title = transcriptURL.split('/')[2]
		print ( url)
		print (episode_title)
		driver.get(url)
		page = driver.page_source

		soup = BeautifulSoup(page, 'lxml')
		div = soup.find(id="mw-content-text").find_all('ul')[0]
		items = [item.text for item in div.select('li')]

		#Display episode title header
		f.write(separator)
		f.write(episode_title + "\n")
		f.write(separator)
		for item in items:
			f.write(item)

driver.quit()

