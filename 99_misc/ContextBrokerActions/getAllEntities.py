__author__ = 'Annika'


# set the following values!
# ----------------------------------------------------------------------------------------------------------------------
ip = "137.226.75.120"
port = "1026"
# ----------------------------------------------------------------------------------------------------------------------


import requests

header = {"Content-Type" : "application/json", "Accept"	 : "application/json"}
urlCB = "http://" + ip + ":" + port + "/v1/"

response = requests.get(url = urlCB + 'contextEntities', headers = header)
allEntitiesJSON = response.json()

if "errorCode" in allEntitiesJSON:
    print("\nNo entities on context broker.")
    quit()

print("\nNumber of entities on", ip, "/", port, ":", len(allEntitiesJSON["contextResponses"]))
for i in range(len(allEntitiesJSON["contextResponses"])):
    entityID = allEntitiesJSON["contextResponses"][i]["contextElement"]["id"]
    entityType = allEntitiesJSON["contextResponses"][i]["contextElement"]["type"]
    entityAttributesList = allEntitiesJSON["contextResponses"][i]["contextElement"]["attributes"]
    print("\nEntity ID", entityID, "( Type", entityType, "):")

    print("Attributes:")
    for attr in entityAttributesList:
        name = attr["name"]
        value = attr["value"]
        print("\t", name, ":", value)

