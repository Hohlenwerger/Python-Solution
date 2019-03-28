# Author: HohlenwergerMB
# *Indented by tabs*

# JSON Utils Import
from jsonUtils import jsonReader, jsonWriter

# READ
data = jsonReader("broken-database.json")	

# FIX
try: # Fix one by one
	for keys in data:
		if type(keys["price"]) == str:
			# Just Parse Float
			keys["price"] = float(keys["price"])
except:
	print("\nError: Price could not be parsed.")
	exit()
	
# WRITE
data = jsonWriter(data, "broken-database.json")	

# END	
print("\nEverything works! Prices in JSON DB were repaired.")