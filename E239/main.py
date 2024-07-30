# Solution E239

with open("f1.txt") as f1:
	l1 = f1.readlines()

with open("f2.txt") as f2:
	l2 = f2.readlines()

# Find the common elements between l1 and l2
res = [n for n in l1 if n in l2]

# Write the result to a file called res.txt
with open("res.txt", "w") as f:
	for n in res:
		f.write(n)
