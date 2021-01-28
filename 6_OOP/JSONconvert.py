import json

# json string
json_string = '{   "name":"tanvir",   "age":22,    "country":"bangladesh"   }'


# parse to dictionary
json_dict = json.loads(json_string)
print(" Dictionary : ",json_dict)



# convert to json_string again
new_json_string = json.dumps(json_dict)
print("JSON_String : ",new_json_string)

