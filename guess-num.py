import random
i = random.randint(1, 100)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == i:
		print('終於猜對了！')
		break
	elif num > i:
		print('比答案大')
	elif num < i:
		print('比答案小')