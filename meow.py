def beta():
	def alpha(val):
		if val:
			print(0)
			return "meow"
		else:
			print(1)
			return alpha(not val)
	print(alpha(False))
beta()