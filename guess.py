import random

r = random.randint(1, 100)
while True:
	n = input('猜一個數子(1~100):')
	n = int(n)
	if n == r:
		print('終於猜對了!')
		break
	elif n < r:
		print('比答案小')
	elif n > r:
		print('比答案大')