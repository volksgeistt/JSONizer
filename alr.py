import json
import random
import string

def genRandomID(existingIDs, length=12):
    while True:
        randomID = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if randomID not in existingIDs:
            existingIDs.add(randomID)
            return randomID

def convertLinkToJSON(inputFile, outputFile):
    jsonify = []
    existingIDs = set()
    with open(inputFile, 'r') as file:
        links = file.readlines()
    for link in links:
        link = link.strip()
        if link:
            linkObject = {
                "url": link,
                "id": genRandomID(existingIDs)
            }
            jsonify.append(linkObject)
    with open(outputFile, 'w') as file:
        json.dump(jsonify, file, indent=2)

    print(f"[!] ~ Switched {len(jsonify)} Lines To JSON Format.")

inputFile = input("[+] ~ Enter Filename Containing The Links >> ") 
outputFile = input("[+] ~ Enter Filename For The Output ( Eg. test.json ) >> ") 
convertLinkToJSON(inputFile, outputFile)
