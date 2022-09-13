import random
import time

Genes = []
GenesScore = []
GeneCount = 100
GeneLength = 30
Answer = "000000000011111111112222222222"

# ================= file save =================
def WriteGene():
	with open("gene.csv", "a") as f:
		f.write(f"{GeneGeneration * GeneCount}\t{TopGene}\t{TopScore}\n")

def GetGene():
	global Gene
	with open("gene.csv", "r") as f:
		Gene = f.readline()

# ================= gene generate =================
def GenerateGene():
	Value = ""
	for _ in range(GeneLength):
		Value += str(random.randrange(0, 3))
	return Value

def CheckGene(Value):
	Score = 0
	for i in range(len(Answer)):
		if Value[i] == Answer[i]:
			Score += 1
	return Score

def ChangeForward(OriginalValue):
	Value = ""
	for _ in range(int(GeneLength / 2)):
		Value += str(random.randrange(0, 3))
	return Value + OriginalValue[int(GeneLength / 2):]

def ChangeBackward(OriginalValue):
	Value = ""
	for _ in range(int(GeneLength / 2)):
		Value += str(random.randrange(0, 3))
	return OriginalValue[:int(GeneLength / 2)] + Value

def ChangeRandomOne(OriginalValue):
	RandomValue = random.randrange(0, GeneLength)
	OriginalValue = list(OriginalValue)
	OriginalValue[RandomValue] = str(random.randrange(0, 3))
	OriginalValue = "".join(OriginalValue)
	return OriginalValue

for _ in range(GeneCount):
	Genes.append(GenerateGene())
	GenesScore.append(0)


GeneGeneration = 1

while True:
	# Get Score
	for i in range(GeneCount):
		GenesScore[i] = CheckGene(Genes[i])

	# Get Top Value
	TopScore = 0
	TopGene = ""
	for i in range(GeneCount):
		if GenesScore[i] > TopScore:
			TopScore = GenesScore[i]
			TopGene = Genes[i]


	# Shake
	for i in range(GeneCount):
		# if i <= GeneCount * ( 45 / 100 ):
		# 	# 45%
		# 	Genes[i] = ChangeForward(Genes[i])
		# elif i <= GeneCount * ( 90 / 100 ):
		# 	# 45%
		# 	Genes[i] = ChangeBackward(Genes[i])
		# else:
		# 	# 10%
		# 	Genes[i] = TopGene

		Genes[i] = ChangeRandomOne(Genes[i])
		
	# Genes[GeneCount - 1] = TopGene
	Genes[0] = TopGene

	if GeneGeneration < 50:
		print(GeneGeneration * GeneCount, TopGene, TopScore)
		WriteGene()

	elif GeneGeneration < 1000:
		if GeneGeneration % 200 == 0:
			print(GeneGeneration * GeneCount, TopGene, TopScore)
			WriteGene()
	else:
		if GeneGeneration % 5000 == 0:
			print(GeneGeneration * GeneCount, TopGene, TopScore)
			WriteGene()

	GeneGeneration += 1

	