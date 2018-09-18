import scipy.integrate as integrate
import math
import numpy
import sys
import matplotlib.pyplot as plt

def main():
	n = int(sys.argv[1]) # Number of Miners
	ittr = int(sys.argv[2]) # Number of Ittr
	#d = float(sys.argv[2]) # Distribution time

	#n = 100 #Number of Miners
	m = 100 #Number of blocks in the Future
	#d = 2 #Distribution Time
	alpha = 1.0 / (n * 14.0)

	forks = 0.0
	x = list()
	y = list()
	contFork = 0.0
	yTheo = list()
	blockLength = 100
	totalOccurences = [0]*(m+1)
	occurences = list()
	mu = 100.0

	allTimes = []
	for k in range(0, ittr):
		if k%100 == 0:
			print "Progress =", k
		forkList = list()
		for j in range(0, blockLength):
			d = numpy.random.exponential(scale=(mu), size=None);
			blockDiscoveryTimes = list()
			for i in range(0, n):
				blockDiscovery = numpy.random.exponential(scale=(n*14.0), size=None)
				allTimes.append(blockDiscovery)
				blockDiscoveryTimes.append(blockDiscovery)

			blockDiscoveryTimes.sort()
			if((float(blockDiscoveryTimes[1]) - float(blockDiscoveryTimes[0])) < float(d)): #Fork
				forks = forks + 1
				contFork = contFork + 1
			else:
				contFork = 0
			forkList.append(contFork)
		occurences.append(forkList)

	x = list()
	once = 0
	fiveNines = 0
	zeroOccurences = 0
	for i in range(0, m+1):
		x.append(i)
		for j in range (0, len(occurences)):
			if i == 0:
				totalOccurences[i] += occurences[j].count(i)
			if i > 0:
				for k in range(0, m-i):
					totalOccurences[i] += occurences[j].count(i+k)
		totalOccurences[i] = totalOccurences[i] / (float(blockLength)*float(ittr))
		#cdf = (1 - math.exp((-(1.0/(14.0)) * d)))
		cdf = ((1.0/(14.0)) / ( (1.0/(14.0)) + (1.0 / mu)))
		if i == 0:
			yTheo.append(1-cdf)
		else:
			yTheo.append(cdf**(i))
		if yTheo[i] < 0.00001 and once == 0:
			fiveNines = i
			once = 1

		#yTheo.append((1-(1-cdf)**(n-1))**(i+1))
	#print totalOccurences
	#print yTheo
	print fiveNines
	plt.plot(x, totalOccurences)
	plt.plot(x, yTheo)
	plt.legend(["Simulation", "Theoretical"])
	plt.xlabel("Age", fontsize=12)
	plt.ylabel("Probability", fontsize=12)
	plt.xlim((0, 10))
	plt.title("Simulation vs theoretical model: n=" + str(n) + " & E[d] =" + str(mu) + "s")
	plt.figure()
	plt.hist(allTimes, bins=50, histtype='bar', rwidth=0.75, normed=True, label='measurements')
	plt.show()
	#print forks / (float)(ittr)

def printBlockAge():
	n = int(sys.argv[1]) # Number of Miners
	ittr = int(sys.argv[2]) # Number of Ittr
	#d = float(sys.argv[2]) # Distribution time

	n = 100 #Number of Miners
	fiveNinesArray = []
	x = []
	for mu in range(1, 101, 1):
		m = 100 #Number of blocks in the Future
		#d = 2 #Distribution Time
		alpha = 1.0 / (n * 14.0)

		forks = 0.0
		contFork = 0.0
		yTheo = []
		blockLength = 100
		totalOccurences = [0]*(m+1)
		occurences = []
		#mu = 1.0
		x.append(mu)
		allTimes = []
		once = 0
		for i in range(0, m+1):
			cdf = ((1.0/(14.0)) / ( (1.0/(14.0)) + (1.0 / mu)))
			if i == 0:
				yTheo.append(1-cdf)
			else:
				yTheo.append(cdf**(i))
			if yTheo[i] < 0.00001 and once == 0:
				fiveNines = i
				once = 1

			#yTheo.append((1-(1-cdf)**(n-1))**(i+1))
		#print totalOccurences
		#print yTheo
		print "delay: " + str(mu) + "fiveNines: " + str(fiveNines)
		fiveNinesArray.append(fiveNines)
	plt.plot(x, fiveNinesArray)
	plt.show()
	#print forks / (float)(ittr)

def varyingN():
	n = int(sys.argv[1]) # Number of Miners
	ittr = int(sys.argv[2]) # Number of Ittr
	#d = float(sys.argv[2]) # Distribution time
	steps = [10, 50, 100]
	for n in steps:
		#n = 100 #Number of Miners
		m = 100 #Number of blocks in the Future
		#d = 2 #Distribution Time
		alpha = 1.0 / (n * 14.0)

		forks = 0.0
		x = []
		y = []
		contFork = 0.0
		yTheo = []
		blockLength = 100
		totalOccurences = [0]*(m+1)
		occurences = []
		mu = 10.0

		for k in range(0, ittr):
			if k%100 == 0:
				print "Progress =", k
			forkList = []
			for j in range(0, blockLength):
				d = numpy.random.exponential(scale=(mu), size=None);
				blockDiscoveryTimes = []
				for i in range(0, n):
					blockDiscovery = numpy.random.exponential(scale=(n*14.0), size=None)
					blockDiscoveryTimes.append(blockDiscovery)

				blockDiscoveryTimes.sort()
				if((float(blockDiscoveryTimes[1]) - float(blockDiscoveryTimes[0])) < float(d)): #Fork
					forks = forks + 1
					contFork = contFork + 1
				else:
					contFork = 0
				forkList.append(contFork)
			occurences.append(forkList)

		x = []
		zeroOccurences = 0
		for i in range(0, m+1):
			x.append(i)
			for j in range (0, len(occurences)):
				if i == 0:
					totalOccurences[i] += occurences[j].count(i)
				if i > 0:
					for k in range(0, m-i):
						totalOccurences[i] += occurences[j].count(i+k)
			totalOccurences[i] = totalOccurences[i] / (float(blockLength)*float(ittr))
			#cdf = (1 - math.exp((-(1.0/(14.0)) * d)))
			cdf = ((1.0/(14.0)) / ( (1.0/(14.0)) + (1.0 / mu)))
			if i == 0:
				yTheo.append(1-cdf)
			else:
				yTheo.append(cdf**(i))

			#yTheo.append((1-(1-cdf)**(n-1))**(i+1))
		print totalOccurences
		plt.plot(x, totalOccurences)
	plt.plot(x, yTheo)
	plt.legend(["Simulation n=10", "Simulation n=50", "Simulation n=100","Theoretical"])
	plt.xlabel("Age", fontsize=12)
	plt.ylabel("Probability", fontsize=12)
	plt.xlim((0, 10))
	plt.title("Simulation vs theoretical model: E[d] = " + str(mu) + "s")
	plt.show()
	#print forks / (float)(ittr)




def timeCorrelation():
	n = int(sys.argv[1])
	d = float(sys.argv[2])
	ittr = int(sys.argv[3])

	m = 10 #Number of blocs in the Future
	alpha = 1.0 / (n * 14.0)

	x = list()
	y = list()
	yTheo = list()
	forkList = list()
	for t in range(1, int(d)):
		print "Progress =", t
		#Theoretical
		cdf = 1 - math.exp((-(1.0/(n*14.0)) * t))
		yTheo.append((1-(1-cdf)**(n-1)))

		x.append(t)
		contFork = 0.0
		forks = 0.0
		for j in range(0, ittr):
			blockDiscoveryTimes = list()

			for i in range(0, n):
				blockDiscovery = numpy.random.exponential(scale=(n*14), size=None)
				blockDiscoveryTimes.append(blockDiscovery)

			blockDiscoveryTimes.sort()
			if((blockDiscoveryTimes[1] - blockDiscoveryTimes[0]) < t): #Fork
				forks = forks + 1
				contFork = contFork + 1
			else:
				contFork = 0
			forkList.append(contFork)

		y.append(forks / (float)(ittr))

	#print forkList
	plt.plot(x, y)
	plt.plot(x, yTheo)
	plt.legend(["Simulation", "Theoretical"])
	plt.xlabel("Distribution Time")
	plt.ylabel("Probability of Fork")
	plt.show()


if __name__ == "__main__":
	#main()
	printBlockAge()
	#varyingN()
	#timeCorrelation()
	