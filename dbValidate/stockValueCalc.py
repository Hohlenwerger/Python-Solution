# Author: HohlenwergerMB
# *Indented by tabs*

# JSON Utils Import
from jsonUtils import jsonReader

# READ
data = jsonReader("broken-database.json")
	
TSBC = []; # Total Stock By Category
categoryList = [] # Categories' Name List

# Iterate Through DB Indexes
for keys in data:
		
	# When a new category id found
	if keys["category"] not in categoryList:
		# Add Category to the List
		categoryList.append(keys["category"])
		# Add Category Initial Stock Value
		TSBC.append(keys["price"] * keys["quantity"])

	else:
		# Find Category Index
		index = categoryList.index(keys["category"])
		# Add Stock Value
		TSBC[index] += keys["price"] * keys["quantity"]
		# Beautify
		TSBC[index] = round(TSBC[index], 2)

print("")
			
# Print Lists			
for i in range(0, len(categoryList)):
		print("Categoria: " + categoryList[i] + " | Valor Total: " + str(TSBC[i]))


''' Uncomment to show that DB is now Fixed by creating an new JSON file called "fixed-database"
	-> It's necessary to import jsonWriter in the top of this code. E.g. * from jsonUtils import jsonWriter *
'''
#jsonWriter(data, "fixed-database.json")

		