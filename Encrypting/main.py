import time
from uncoding import *
from random import randint

BITS_LIST = (1,2,4,8,16,32,64,128,256)
CODING_LAYOUTS = ('mult')

def generationPassword(len_password):
	password = ''
	for i in range(len_password):
		password += str(randint(0,9))
	return password

class login:
	def __init__(self,password, min_len = 6, max_len = 16):
		if len(str(password)) < min_len:
			raise ValueError('In password must have 6 letter or more!')
		elif len(str(password)) > max_len:
			raise ValueError('In password must have 16 letter or less!')
		else:
			self.__password = password

	def login(self,loginPassword):
		log = True if str(loginPassword) == str(self.__password) else False
		return log

	def set_pass(self,newpassword):
		self.__password = newpassword
		return newpassword


class Coding:
	def __init__(self):
		self.__key = ''

	def checkKey(self):
		if not self.__key:
			raise ValueError('You don\'t have key!')

	def setKey(self, bits = 8, type_coding = CODING_LAYOUTS[0]):
		self.__key = ''
		if type_coding == CODING_LAYOUTS[0]:
			if bits in BITS_LIST:
				for i in range(bits):
					self.__key+=str(randint(1,9))
			else:
				raise ValueError('Bit Error! [BITS_LIST - all bits]')
		return self.__key

	def getKey(self):
		self.checkKey()
		return self.__key

	def delKey(self):
		self.checkKey()
		self.__key = ''

	def codPassword(self, password, type_coding = CODING_LAYOUTS[0], key = None):
		key = str(key) if key else self.__key

		assert key, 'You don\'t have password!'

		newCode = ''
		if type_coding == CODING_LAYOUTS[0]:
			newCode = str(int(password)*int(key))

		return newCode

	def uncodPassword(self, codingpassword, type_coding = CODING_LAYOUTS[0], key = None):
		key = str(key) if key else self.__key

		assert key, 'You don\'t have password!'

		newCode = ''
		if type_coding == CODING_LAYOUTS[0]:
			newCode = str(int(int(codingpassword)/int(key)))

		return newCode

#test
if __name__ == '__main__':
	firstTime = time.time()
	myPassWord = generationPassword(6)
	print(myPassWord)
	account = login(myPassWord)

	cd = Coding()
	key = cd.setKey(bits=8); print('Key:'+str(key))
	codingPass = cd.codPassword(myPassWord); print('Coding password:'+str(codingPass))
	uncodingPass = cd.uncodPassword(codingPass); print('Uncoding password:'+str(uncodingPass))
	
	print(account.login(uncodingPass))
	print('\n')
	
	possiblePassword = uncodingNum(codingPass, output = True)
	[print('Password: '+str(password)) for password in possiblePassword if account.login(password)]
	secondTime = time.time()
	print('Time: ',str(secondTime - firstTime))