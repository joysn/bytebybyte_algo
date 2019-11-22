# 26. Smallest Change
# ● Question: Given an input amount of change x, write a function to determine the
# minimum number of coins required to make that amount of change.
# ● Eg. (using American coins) 1, 5, 10, 25
# change(1) = 1
# change(3) = 3
# change(7) = 3
# change(32) = 4


coins = [1,5,10,25]

def change(amount):
	if amount == 1:
		return 1
	elif amount == 0:
		return 0
	else:
		min_coins = 100000
		for den in reversed(coins):
			if amount - den >= 0:
				num_of_coins = 1 + change(amount - den)
				if num_of_coins < min_coins:
					min_coins = num_of_coins
		return min_coins

print("1$ needs ",change(1)," # of coins")
print("3$ needs ",change(3)," # of coins")
print("7$ needs ",change(7)," # of coins")
for i in range(32,41):
	print(i,"$ needs ",change(i)," # of coins")
	

# (base) D:\>python int26_number_of_coins.py
# 1$ needs  1  # of coins
# 3$ needs  3  # of coins
# 7$ needs  3  # of coins
# 32 $ needs  4  # of coins
# 33 $ needs  5  # of coins
# 34 $ needs  6  # of coins
# 35 $ needs  2  # of coins
# 36 $ needs  3  # of coins
# 37 $ needs  4  # of coins
# 38 $ needs  5  # of coins
# 39 $ needs  6  # of coins
# 40 $ needs  3  # of coins

