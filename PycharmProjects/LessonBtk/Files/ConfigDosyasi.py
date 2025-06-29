import json

user_info={
    "username":"admin",
    "password":"1234"
}

# dosyaya yazma
with open("config.json", "w") as f:
    json.dump(user_info, f)


# dosyadan cekme metodu
def getInfoFromConfig():
    with open("config.json", "r") as f:
        return json.load(f)


info=getInfoFromConfig()
print(info["username"])
print(info["password"])

