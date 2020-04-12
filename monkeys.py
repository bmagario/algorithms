import random

def generateOne(strlen):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	res = ""
	for i in range(strlen):
		res += alphabet[random.randrange(27)]
	return res

def score(goal, testString):
	numSum = 0
	for i in range(len(goal)):
		if goal[i] == testString[i]:
			numSum += 1
	return numSum / len(goal) 

def main():
	goalString = "Hello"
	newString = generateOne(28)
	best = 0
	newScore = score(goalString, newString)
	while newScore < 1:
		if newScore > best:
			print(newScore, newString)
			best = newScore
		newString = generateOne(28)
		newScore = score(goalString, newString)

main()