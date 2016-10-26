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

entityIDs = []
entityTypes = []
for i in range(len(allEntitiesJSON["contextResponses"])):
    entityIDs.append(allEntitiesJSON["contextResponses"][i]["contextElement"]["id"])
    entityTypes.append(allEntitiesJSON["contextResponses"][i]["contextElement"]["type"])

print(entityIDs, entityTypes)

for id, type in zip(entityIDs, entityTypes):
    deleteJSON =    {
                        "contextElements": [ {
                            "type": type,
                            "isPattern": "false",
                            "id": id
                        } ],
                        "updateAction": "DELETE"
                    }

    response = requests.post(url = urlCB + 'updateContext/', headers = header, json = deleteJSON)
