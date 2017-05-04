
class CalcHMM:
	wB, hB 	= 3,2;
	wA, hA 	= 2,2;
	B 		= [[0 for x in range(3)] for y in range(2)]
	A 		= [[0 for x in range(2)] for y in range(2)]
	O 		= [0,1,2,0]
	X 		= [0,0,1,1]
	T 		= 0
	lamb	= [0.6, 0.4]

	def __init__(self):
		self.B[0][0] = 0.1
		self.B[0][1] = 0.4
		self.B[0][2] = 0.5

		self.B[1][0] = 0.7
		self.B[1][1] = 0.2
		self.B[1][2] = 0.1

		self.A[0][0] = 0.7
		self.A[0][1] = 0.3
		
		self.A[1][0] = 0.4
		self.A[1][0] = 0.6

	def FWAlgorithm(self,timeT,stateI):
		if timeT == 0:
			return self.lamb[stateI]*self.B[stateI][self.O[0]]
		else:
			ati = 0
			for X in range (0,2):
				ati += self.FWAlgorithm(timeT-1,X)*self.A[X][stateI]
			ati *= self.B[stateI][self.O[timeT]]
			return ati

	def BWAlgorithm(self,timeT,stateI):
		if timeT == len(self.O)-1:
			return 1
		else:
			bti = 0
			for x in range (0,2):
				bti += self.A[stateI][x]*self.B[x][self.O[timeT+1]]*self.BWAlgorithm(timeT+1,x)
			return bti

	def prob_likehoodOfO(self):
		retVal = 0
		#2=jumlah defined state
		for X in range(0,2):
			retVal += self.FWAlgorithm(3,X)
		return retVal

	def yti(self,timeT,stateI):
		a = self.FWAlgorithm(timeT,stateI)
		b = self.BWAlgorithm(timeT,stateI)
		return (a*b)/self.prob_likehoodOfO()

	def maxValue(self,array):
		min = 0
		for x in range (1,len(array)):
			if array[x]>array[min]:
				min = x
		return min

	def mostLikelyStatePath(self):
		probOfState = [0,0]
		state = [0 for y in range(len(self.O))]
		for x in range (0,len(self.O)):
			for y in range (0, len(probOfState)):
				probOfState[y] = self.yti(x,y)
			state[x] = self.maxValue(probOfState)
		return state



H = CalcHMM()
array = H.mostLikelyStatePath()
print(H.prob_likehoodOfO())
print(H.yti(3,0))
print(array)


