import json

with open("day.json") as testFile:
    jsonObject = json.load(testFile)
    testFile.close()
    
temp = jsonObject('temp')

print(temp)