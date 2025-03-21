# Common street names analyzer
---


Currently the Data source used is [openaddresses.org](https://batch.openaddresses.io/data#map=0/0/0).
This website splits all geo location data into sections of the US. The format of this data is a [geojson](https://geojson.org/) file
    

Future plans (Personal Notes)

1. Load all the data into an SQLite database (maybe mysql if this takes off)
2. Find a way to better aggregate the data, maybe in the future I want more than just street names since this data includes other geo data too


Personal Notes:

- Data can now load into MySQL, next we want to make sure we dont insert duplicates into the database

### Database

1. Create a new SQLite db in the root of the repo called `csn.db`
2. Create a new table within the db called `GeoAddress`
```sql
CREATE TABLE "GeoAddress" (
	"id"	INTEGER,
	"lat"	REAL,
	"lon"	REAL,
	"city"	TEXT,
	"district"	TEXT,
	"number"	TEXT,
	"zip_code"	TEXT,
	"streetname"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```