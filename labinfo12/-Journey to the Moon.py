def go():
	I=lambda:map(int,input().split())
	n,l=I()
	d=list(range(n))
	def f(a):
		if d[a]!=a:d[a]=f(d[a])
		return d[a]
	for i in range(l):
		a,b=I()
		d[f(a)]=f(b)
	q=[0]*n
	for i in range(n):q[f(i)]+=1
	print(sum(i*(n-i)for i in q)//2)

go()