# Author: HohlenwergerMB
# *Indented by tabs*

# JSON Utils Import
from jsonUtils import jsonReader, jsonWriter

# READ
data = jsonReader("broken-database.json")	

# FIX
try: # Fix one by one
	temp = {}
	for keys in data:
		if "quantity" not in keys:
			# Add the missing key
			keys["quantity"] = 0
			
			# Swap positions
			# Just necessary if the order of Array keys is important
			keys["price"] = keys.pop("price")
			keys["category"] = keys.pop("category")
			
except:
	print("\nError: Failed to create a new key 'quantity' with value 0.")
	exit()
	
# WRITE
jsonWriter(data, "broken-database.json")

# END	
print("\nEverything works! Quantities in JSON DB were repaired.")