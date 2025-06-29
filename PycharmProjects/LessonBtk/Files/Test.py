import os, json

myInfo = {
    "username":"admin",
    "password":"1441",
    "url":"https://www.google.com"
}

configPath ="C:/Users/fakha/DERSLER/PYTHON/PycharmProjects/LessonBtk/configs/config.json"
filePath = os.getcwd()
print(configPath)
print(filePath)

with open(configPath, "w") as f:
    json.dump(myInfo, f)

def getInfoFromConfigJson():
    with open(configPath, "r") as f:
        return json.load(f)


info = getInfoFromConfigJson()
print(info["username"])
print(info["password"])
print(info["url"])


