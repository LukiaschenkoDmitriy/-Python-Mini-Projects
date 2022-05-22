import math

def fibonacсi_nums(max_repeat = 1000):
	fibonacсi_num_array = [0,1]
	for i in range(max_repeat):
		fibonacсi_num_array.append(fibonacсi_num_array[-1]+fibonacсi_num_array[-2])
	return fibonacсi_num_array

#f_St(n,k) = f_St(n-1,k-1) + k * f_St(n-1,k)

def f_St(n,k):
	if n >= k:
		if n == k or k == 1:
			return 1
		elif k == 0:
			return 0
		else:
			return f_St(n-1,k-1) + k * f_St(n-1,k)
	else:
		return 0

def f_Catalana(n):
	if n >= 1:
		result = 0
		for i in range(n):
			result += f_Catalana(i)*f_Catalana(n-1-i)
		return result
	return 1

def f_Bl(n):
	result = 0
	for m in range(n):
		result += f_St(n,m)
	return result+1

def f_factorial(n):
	result = 1
	for i in range(n):
		i+= 1
		result *= i
	return result

class PropertiesNum:
	def __init__(self, num):
		self.num = num

		self.multipliers_array = []
		self.divisors_array = []
		self.stirling_num_array = []
		self.bell_num_array = []
		self.catalan_num_array = []
		self.factorial_num_array = []

		self.fibonacсi_array = fibonacсi_nums(self.num)

	def multipliers(self):
		self.multipliers_array = []
		for multiplier in range(self.num):
			if multiplier > 1:
				if self.num/multiplier == int(self.num/multiplier):
					self.multipliers_array.append(multiplier)
		return self.multipliers_array

	def divisors(self):
		self.divisors_array = [1,*self.multipliers(),self.num]
		return self.divisors_array

	def amount_divisort(self):
		return len(self.divisors())

	def sum_divisort(self):
		return sum(self.divisors())

	def prime_num(self):
		if self.amount_divisort() == 2:
			return True
		return False

	def fibonacсi(self):
		if self.num in self.fibonacсi_array:
			return True
		return False

	def stirling_num(self):
		self.stirling_num_array = []
		for n in range(20):
			for k in range(20):
				self.stirling_num_array.append(f_St(n,k))

		if self.num in self.stirling_num_array:
			return True
		return False

	def bell_num(self):
		self.bell_num_array = []
		for n in range(20):
			self.bell_num_array.append(f_Bl(n))

		if self.num in self.bell_num_array:
			return True
		return False

	def catalan_num(self):
		self.catalan_num_array = []
		for n in range(10):
			self.catalan_num_array.append(f_Catalana(n))

		if self.num in self.catalan_num_array:
			return True
		return False

	def factorial_num(self):
		self.factorial_num_array = []
		for n in range(20):
			self.factorial_num_array.append(f_factorial(n))

		if self.num in self.factorial_num_array:
			return True
		return False

	def root(self):
		return math.sqrt(self.num)

	def square(self):
		return self.num*self.num

	def get_info(self):
		print(f'Число:{self.num}')
		print('-'*20)
		print(f'Квадрат числа:{self.square()}')
		print(f'Корень числа:{self.root()}')
		print(f'Множители:{self.multipliers()}')
		print(f'Делители:{self.divisors()}')
		print(f'Количество делителей:{self.amount_divisort()}')
		print(f'Сума делителей:{self.sum_divisort()}')
		print(f'Простое число:{self.prime_num()}')
		print(f'Число Фибоначчи:{self.fibonacсi()}')
		print(f'Число Стирлинга:{self.stirling_num()}')
		print(f'Число Белла:{self.bell_num()}')
		print(f'Число Каталана:{self.catalan_num()}')
		print(f'Число - факториал:{self.factorial_num()}')

PropertiesNum(29*29).get_info()


