import json
with open("data.json","r")as file:
    data=json.load(file)
    data ["username"] ="abc"
with open("data.json","w")as file:
    json.dump(data,file,indent=4)
print("sucessfully updated")
