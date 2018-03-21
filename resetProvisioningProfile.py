import os
import glob
import re

#traversal all files
def traversalPrint(file_list):
	print '\n<------------------------------------------------------'
	for i,v in enumerate(file_list):
		print i , '->' , v , '\n'
	print '\n------------------------------------------------------>'

def isNumber(s):
	try:
		int(s)
		return True
	except ValueError:
		pass

	return False

def deleteFile(path):
	if os.path.exists(path):
		os.remove(path)


#delete profiles 
def deleteAllFiles(file_list):
	print '\n<------------------------------------------------------>'
	print 'input <del - index> to delete a file by index,for example -> del - 1'
	print 'input <del - all> to delete all files'
	print 'input <exit> to return to previous menu'

	input = raw_input('Please input:')
	if input == 'exit':
		return

	try:
		input = input.split('-')[1]
	except IndexError:
		print 'invalid input'
		return
	
	input = re.sub('\s', '', input)
	if isNumber(input) == True:
		try:
			filePath = file_list[int(input)]
		except IndexError:
			print ('index out of bounds')
			return

		deleteFile(filePath)
	else:
		if input == 'all':
			for filePath in file_list:
				deleteFile(filePath)
		else:
			print 'invalid input'
#main 


while 1:
	os.chdir('/Users')
	file_list = glob.glob(r'*/Library/MobileDevice/Provisioning Profiles/*.mobileprovision')
	print '\n<------------------------------------------------------>'
	print 'Provisioning Profiles num is :',len(file_list)
	print 'input <m> to show more detail'
	print 'input <del> to delete Profiles'

	input = raw_input('Please input:')
	
	if input == 'm':
		traversalPrint(file_list)
	elif input == 'del':
		deleteAllFiles(file_list)
	else:
		print 'invalid input'

