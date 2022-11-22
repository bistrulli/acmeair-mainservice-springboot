#!/bin/bash 

mongoimport --uri mongodb://localhost:27017 --db=acmeair_customerdb --collection="customer" --file=./acmeair_customerdb.json  --jsonArray

mongoimport --uri mongodb://localhost:27017 --db=acmeair_flightdb --collection="airportCodeMapping" --file=./airportCodeMapping.json  --jsonArray
mongoimport --uri mongodb://localhost:27017 --db=acmeair_flightdb --collection="flight" --file=./flight.json  --jsonArray
mongoimport --uri mongodb://localhost:27017 --db=acmeair_flightdb --collection="flightSegment" --file=./flightSegment.json  --jsonArray