# 1
str1 = 'Hello3World!2'
numbers = []
for x in str1:
	try:
		if int(x):
			numbers.append(int(x))
	except ValueError:
		pass

print (numbers)

# 2
what = input('Что делаем (+, -, /, *) ? : ')

a = float(input('Первое число: '))
b = float(input('Второе число: '))

result = 0
if what == '+':
	result = a + b

if what == '-':
	result = a - b

if what == '/':
	result = a / b

if what == '*':
	result = a * b
else:
	result = 0

print (result)

# 3

even_elements = []

my_list = ['A', 'b', 'c', 234, 'Hello World!']

for x in my_list:
	if my_list.index(x) % 2 == 1:
		even_elements.append(x)

print (even_elements)