import json
h = open('file.json')

data = json.load(h)
for emp in data:
    for key in emp:
        if key=="address":
            print("Address")
            for adds in key:
                print (key[adds])
        print (emp[key])
