import random
# The Coin class simulates a coin that can
# be flipped.
class Coin:
	# The _ _init_ _ method initializes the
	# sideup data attribute with 'Heads'.
	
	def __init__(self):
		## the __ says that the attribute is private ex: __sideup
		self.sideup = 'Heads'

	def toss(self):
		if random.randint(0,1) == 0:
			self.sideup = 'Heads'
		else:
			self.sideup = 'Tails'

	def get_sideup(self):
		return self.sideup

## TEST

def main():
	my_coin = Coin()
	my_coin2 = Coin()

	print("This side is up:", my_coin.get_sideup())

	print('I am tossing the coin...')
	my_coin.toss()
	print('This side is up:', my_coin.get_sideup())
	
	print()
	print()
	
	print("This side is up:", my_coin2.get_sideup())
	tosses = input("How many times do you want to flip the coin?")
	for i in range(tosses):
		my_coin2.toss()
		print(my_coin2.get_sideup())
		

main()
