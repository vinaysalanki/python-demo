import json
data={
    "username":"vinusalanki",
    "game_name":"cod",
    "password": "@123"
}
with open("data.json","w")as file:
    json.dump(data,file,indent=4)
with open("data.json","r")as file:
    data=json.load(file)
print("created sucessfully")