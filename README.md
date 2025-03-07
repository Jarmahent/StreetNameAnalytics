# Common street names analyzer
---


Currently the Data source used is [openaddresses.org](https://batch.openaddresses.io/data#map=0/0/0).
This website splits all geo location data into sections of the US. The format of this data is a [geojson](https://geojson.org/) file
    

Future plans (Personal Notes)

1. Load all the data into an SQLite database (maybe mysql if this takes off)
2. Find a way to better aggregate the data, maybe in the future I want more than just street names since this data includes geopoints too