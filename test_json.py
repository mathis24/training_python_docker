import json

s='{"a":12, "b":[1,2,3]}'		# a string representation of json data
d=json.loads(s)		# convert string into a dictionary
print(d, type(d))		
sback = json.dumps(d)	# convert a dictionary into a string 
                        # (to send via rest api for instance)
print(sback, type(sback))
