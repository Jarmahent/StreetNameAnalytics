import os
from typing import Optional
import geojson
from pydantic import BaseModel
from database import Base, GeoAddress, engine, get_db

# Initialize database
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

class GeometrySchema(BaseModel):
    coordinates: list[float]

class PropertiesSchema(BaseModel):
    city: Optional[str]
    district: Optional[str]
    hash: Optional[str]
    id: Optional[str]
    number: Optional[str]
    postcode: Optional[str]
    region: Optional[str]
    street: Optional[str]
    unit: Optional[str]

class GeoSchema(BaseModel):
    geometry: GeometrySchema
    properties: PropertiesSchema


class GeoJSONProcessor:

    def __init__(self, asset_path: str, delete_meta: bool = True, verbose: bool = True):
        self.asset_path = asset_path
        self.geojson_ext = "geojson"
        self.meta_ext = "meta"
        self.verbose = verbose

        if delete_meta:
            print("Deleting meta...")
            for root, dirs, files in os.walk(self.asset_path):
                for file in files:
                    if file.endswith(self.meta_ext):
                        final_path = os.path.join(root, file)
                        os.remove(final_path)

    def parse(self, file)-> list[GeoSchema]:
        final_path = os.path.join(root, file)
        if self.verbose:
            print(f"Loading in {file}")
        with open(final_path, "r") as geojsonfile:
            raw_geojson = geojsonfile.read()
            split_json = raw_geojson.split("\n")
            total_nodes = len(split_json)
            geojson_arr = []
            for index, geojson_obj in enumerate(split_json):
                try:
                    if index == 3000:
                        break
                    if self.verbose:
                        print(f"At {index} out of {total_nodes}")
                    parsed_geojson = geojson.loads(geojson_obj)
                    validated_geojson = GeoSchema.model_validate(parsed_geojson)
                    geojson_arr.append(validated_geojson)
                except Exception as e:
                    if self.verbose:
                        print(f"Failed at {index}")
            return geojson_arr


gjp = GeoJSONProcessor(asset_path="./assets", delete_meta=False, verbose=False)

session = get_db()
for session in session:
    for root, dirs, files in os.walk(gjp.asset_path):
        for file in files:
            if file.endswith(gjp.geojson_ext) and "addresses" in file:
                ggf = gjp.parse(file)
                for geo in ggf:
                    geot = GeoAddress(
                        lat=geo.geometry.coordinates[0],
                        lon=geo.geometry.coordinates[1],
                        city=geo.properties.city,
                        district=geo.properties.district,
                        number=geo.properties.number,
                        zip_code=geo.properties.postcode,
                        streetname=geo.properties.street,
                    )
                    session.add(geot)

                session.commit()

                break    
            