import random
i = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字:')
	num = int(num)
	if num == i:
		print('終於猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif num > i:
		print('比答案大')
	elif num < i:
		print('比答案小')
	print('這是你猜的第', count, '次')