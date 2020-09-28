import time

def calcProd():
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The product is %s digits long' % (len(str(prod))))
print('The program run in %s seconds' % (endTime - startTime))

