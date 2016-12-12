def getCurrentStatus():
	currentPointsEarned = 0
	categories = 1
	contributionToFinal = 100
	option = ""
	while option != "n":
		grade = input("\n	Category " + str(categories) + " average: ")
		weight = input("	Category " + str(categories) + " weight(%): ")
		currentPointsEarned += grade*weight/100.0
		categories += 1
		contributionToFinal -= weight
		option = raw_input("Do you have another category? (y/n): ")
	returnInfo = [currentPointsEarned, contributionToFinal]
	print ""
	return returnInfo

def getGradingScale(className):
	option10 = raw_input("Does " + className + " use a 10 point grading scale? (y/n):	")
	optionPlus = raw_input("Does " + className + " use plus grades (A+, B+,)? (y/n):	")
	optionMinus = raw_input("Does " + className + " use minus grades (A-, C-)? (y/n):	")
	
	if option10 == "y" and optionPlus == "y" and optionMinus == "y":
		gradingScale = {"A+" : 97, "A" : 93, "A-" : 90, "B+" : 87, "B" : 83, "B-" : 80, "C+" : 77, "C" : 73, "C-" : 70, "D" : 60}
	elif option10 == "y" and optionPlus == "y" and optionMinus == "n":
		gradingScale = {"A+" : 97, "A" : 90, "B+" : 87, "B" : 80, "C+" : 77, "C" : 70, "D" : 60}
	elif option10 == "y" and optionPlus == "n" and optionMinus == "y":
		gradingScale = {"A" : 93, "A-" : 90, "B" : 83, "B-" : 80, "C" : 73, "C-" : 70, "D" : 60}
	elif option10 == "y" and optionPlus == "n" and optionMinus == "n":
		gradingScale = {"A" : 90, "B" : 80, "C" : 70, "D" : 60}
	else:
		gradingBenchmarks = input("How many grades are there? ")
		for grades in range(gradingBencharks):
			grade = raw_input("Grade: ")
			benchmark = input("Minimum average: ")
			if grades == 0:
				gradingScale = {grade, benchmark}
			else:
				gradingScale[grade] = benchmark
	return gradingScale

def calculateRequiredGrade(currentPointsEarned, contributionToFinal, goalAverage):
	return (goalAverage - currentPointsEarned)/(contributionToFinal/100.0)


className = raw_input("Class name:	")
currentStatus = getCurrentStatus()
currentPointsEarned = currentStatus[0]
contributionToFinal = currentStatus[1]
gradingScale = getGradingScale(className)

print "\n\n\t\tMINIMUM GRADE CALCULATOR\n"
option = raw_input("\nPlease choose from the following options: \n\t(1) - View Current Average \n\t(2) - View Required Grade For A Specific Grade \n\t(3) - View a table for every grade\\n\t(10) - Choose a new class\n\t(11) - Enter a new grading scale \n\t(12) - Change your grades\n\t(99) - Exit\nOption: ")
while option != "99":
	if option == "1":
		print "\nYour Current Grade in " + className + " is " + str(currentPointsEarned / (100.0 - contributionToFinal))
	elif option == "2":
		goalGrade = raw_input("What grade are you trying to earn? (A+, B, C-, etc): ")
		try:
			goalAverage = gradingScale[goalGrade]
			requiredGrade = calculateRequiredGrade(currentPointsEarned, contributionToFinal, goalAverage)
			print "You must earn at least " + str(requiredGrade) + " in " + className + " to acheive a " + goalGrade
		except Exception:
			print "invalid grade"
	elif option == "3":
		print "\n\t" + className 
		for item in range(len(gradingScale)):
			print str(item) 
			thisGrade = gradingScale.keys()[item]
			print thisGrade
			thisGoal = gradingScale[thisGrade]
			print thisGrade + "\t:\t" + str(calculateRequiredGrade(currentPointsEarned, contributionToFinal, thisGoal))
##FINDOUT WHY THE LIST IS OUT OF ORDER
	elif option =="10":
		className = raw_input("New class name:	")
		currentStatus = getCurrentStatus()
		currentPointsEarned = currentStatus[0]
		contributionToFinal = currentStatus[1]
		gradingScale = getGradingScale(className)
	elif option == "11":
		gradingScale = getGradingScale(className)
	elif option == "12":
		currentStatus = getCurrentStatus()
		currentPointsEarned = currentStatus[0]
		contributionToFinal = currentStatus[1]			
	option = raw_input("\nPlease choose from the following options: \n\t(1) - View Current Average \n\t(2) - View Required Grade For A Specific Grade \n\t(3) - View a table for every grade\n\t(10) - Choose a new class\n\t(11) - Enter a new grading scale \n\t(12) - Change your grades\n\t(99) - Exit\nOption: ")








