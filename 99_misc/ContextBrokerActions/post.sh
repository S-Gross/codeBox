if test -z "$3" ; then
	echo "usage: $0 <entity> <aname> <avalue> [atype]"
	exit
fi

ID=$1
NAME=$2
VALUE=$3
TYPE=$4

if test -n $4 ; then
	QUERY="\"attributes\" : [ { \"name\" : \"$NAME\", \"type\" : \"$TYPE\", \"value\" : \"$VALUE\" } ]"
else
	QUERY="\"attributes\" : [ { \"name\" : \"$NAME\", \"value\" : \"$VALUE\" } ]"
fi

echo "{$QUERY}" | curl 137.226.75.89:1026/ngsi10/contextEntities/$ID -X POST -s -S --header 'Content-Type: application/json' --header 'Accept: application/json' -d @-
echo "{$QUERY}"

