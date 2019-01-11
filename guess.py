import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	n = input('猜一個數子(1~100):')
	n = int(n)
	if n == r:
		print('終於猜對了!')
		print('這是你猜的', count, '次')
		break
	elif n < r:
		print('比答案小')
	elif n > r:
		print('比答案大')
	print('這是你猜的', count, '次')