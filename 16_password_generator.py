#password_recommend = ['Your password must contain minimum 8 characters, a special symbol, an upper case letter and a number',
#					  'password must be at least 8 characters long',
#					  'special symbols can be only one of the following : !,@,#,$,%,^,&,*',
#					  'password requires at least 1 upper case letter',
#					  'password requires at least 1 special character',
#					  'password requires at least 1 number']
#
#print (password_recommend[0])
#password_str = input('Enter a password:')
#password_len = len(password_str)
#trial = 3
#
#if (password_len < 8):
#	print (password_recommend[1])
#	trial -= 1
#	if (trial < 3):

import random
import string
pass_len = int(input("How long do you want your password to be ? : "))
passwd = []
symbol_list = ['~','!','@','#','$','%','^','&','+','_']
while (i < pass_len):
	passwd.append(random.sample(symbol_list))