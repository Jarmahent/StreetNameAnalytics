import os
import geojson

class GeoJSONProcessor:

    def __init__(self, asset_path: str, delete_meta: bool = True):
        self.asset_path = asset_path
        self.geojson_ext = "geojson"
        self.meta_ext = "meta"

        if delete_meta:
            print("Deleting meta...")
            for root, dirs, files in os.walk(self.asset_path):
                for file in files:
                    if file.endswith(self.meta_ext):
                        final_path = os.path.join(root, file)
                        os.remove(final_path)

    def parse(self, file)-> list:
        final_path = os.path.join(root, file)
        print(f"Loading in {file}")
        with open(final_path, "r") as geojsonfile:
            raw_geojson = geojsonfile.read()
            split_json = raw_geojson.split("\n")

            geojson_arr = []
            for index, geojson_obj in enumerate(split_json):
                try:
                    geojson_arr.append(geojson.loads(geojson_obj))
                except Exception:
                    print(f"Failed at {index}")



gjp = GeoJSONProcessor(asset_path="./assets", delete_meta=True)
for root, dirs, files in os.walk(gjp.asset_path):
    for file in files:
        if file.endswith(gjp.geojson_ext):
            ggf = gjp.parse(file)
            print(ggf)
            break    
        