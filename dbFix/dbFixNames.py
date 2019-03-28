# Author: HohlenwergerMB
# *Indented by tabs*

# JSON Utils Import
from jsonUtils import jsonReader, jsonWriter

# READ
data = jsonReader("broken-database.json")	

# FIX
try: # Fix one by one
	for keys in data:
		# First letter of word in upper case
		keys["name"] = keys["name"].replace(' ø', ' O').replace(' æ', ' A').replace(' ¢', ' C').replace(' ß', ' B')

		keys["name"] = keys["name"].replace('ø', 'o').replace('æ', 'a').replace('¢', 'c').replace('ß', 'b')
except:
	print("\nError: Name could not be fixed.")
	exit()
	
# WRITE
data = jsonWriter(data, "broken-database.json")	

# END	
print("\nEverything works! Names in JSON DB were repaired.")