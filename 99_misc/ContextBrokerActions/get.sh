ID=$1

curl 137.226.75.89:1026/ngsi10/contextEntities/$ID -X GET -s -S --header 'Content-Type: application/json' --header 'Accept: application/json'

