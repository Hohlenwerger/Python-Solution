# Author: HohlenwergerMB
# *Indented with tabs*

# Import JSON methods
import json

def jsonReader(file):
	try:
	  # Open JSON file with encoding UTF-8 to prevent problems with special chars
		with open(file, encoding="utf8") as data_file:    
			return json.load(data_file)

	except:
		print("\nError: 'broken-database.json' file could not be open.")
		exit()	
		
def jsonWriter(data, newfile):
	try:
		# Create JSON file with encoding UTF-8 to prevent problems with special chars
		with open(newfile, 'w', encoding="utf8") as outfile:
			# dump indented
			json.dump(data, outfile, ensure_ascii = False, indent = 2)
			
	except:
		print("\nError: Could not save the repaired JSON file.")
		exit()

# Beauty Print ^^
def jsonPrint(data):
	print(json.dumps(data,ensure_ascii = False, indent = 2))