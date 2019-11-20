'''
Remove anchor from URL

ex. 
'www.codewars.com#about' --> 'www.codewars.com'
'www.codewars.com?page=1' --> 'www.codewars.com?page=1'
'''

def remove_url_anchor(url):
	
	try:
		return url[:url.index('#')]
	except:
		return url

