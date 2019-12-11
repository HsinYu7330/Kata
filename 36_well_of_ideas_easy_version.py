'''
Well of Ideas-Easy Version
'''

def well(x):
	
	good_cnt = x.count('good')
	if good_cnt == 0:
		return 'Fail!'
	elif good_cnt <= 2:
		return 'Publish!'
	else:
		return 'I smell a series!'


