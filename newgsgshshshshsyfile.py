s = "The quick brown fox jumps over the lazy dog"
m = s
dic = {"The": "A"}
for r, v in dic.items():
	m = m.replace(r, v)
print(m)
for r in (("brown", "red"), ("lazy", "quick")):
    s = s.replace(*r)
print(s)