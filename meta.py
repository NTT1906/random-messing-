a= {
	"beta": 1,
	"alpha": 2,
	"meta": 3,
	4: "haha",
	3: 5
}
b ={
	"beta": 1,
}
out = dict()
out ={**a, **b}
"""for i in a.keys():
	if i in b:
		out[i] = b[i]
	else:
		out[i] = a[i]
		"""
print("Before:")
print(a)
print(b)
print(out)
print(dict(set(a.items()) - set(b.items())))