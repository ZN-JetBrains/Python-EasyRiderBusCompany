# import json

json_file_name = "users.json"

with open(json_file_name, "r") as json_file:
    user_dict = json.load(json_file)
    print(len(user_dict["users"]))
