# Author: HohlenwergerMB
# *Indented by tabs*

# JSON Utils Import
from jsonUtils import jsonReader, jsonPrint

# READ
badList = jsonReader("broken-database.json")

# Adapted Bubble Sort
length = len(badList) - 1
unsorted = True

while unsorted:
	unsorted = False
	
	for element in range(0,length):
		# Check Category Alphabetical Order
		if badList[element]["category"] > badList[element + 1]["category"]:
			# Swap
			badList[element], badList[element+1] = badList[element+1], badList[element]
			# Mark as not ready, need to check again
			unsorted = True
			
		# If in the same category... 	
		elif badList[element]["category"] == badList[element + 1]["category"]:
			# ...sort by id
			if badList[element]["id"] > badList[element + 1]["id"]:
				# Swap
				badList[element], badList[element+1] = badList[element+1], badList[element]
				# Mark as not ready, need to check again
				unsorted = True

# Put badList's ordained products' name in a list
ordainedList = []
for keys in badList:
	ordainedList.append(keys["name"]);

# Print List								
jsonPrint(ordainedList)