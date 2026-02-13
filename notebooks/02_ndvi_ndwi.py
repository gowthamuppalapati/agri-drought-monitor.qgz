import geopandas as gpd
import numpy as np
from pystac_client import Client
import planetary_computer as pc
import stackstac
import rioxarray  # enables .rio

# 1) Load AOI
aoi = gpd.read_file("data/aoi.geojson").to_crs("EPSG:4326")
geom = aoi.geometry.iloc[0]

# 2) Search Sentinel-2
catalog = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")

time_range = "2026-01-01/2026-02-13"  # change if needed

search = catalog.search(
    collections=["sentinel-2-l2a"],
    intersects=geom.__geo_interface__,
    datetime=time_range,
    query={"eo:cloud_cover": {"lt": 40}}
)

items = list(search.get_items())
print("Found scenes:", len(items))
if len(items) == 0:
    raise SystemExit("No scenes found. Increase cloud limit or widen dates.")

item = pc.sign(items[0])
print("Using scene:", item.id)

# 3) Load bands
stack = stackstac.stack(
    [item],
    assets=["B04", "B08", "B11"],
    epsg=4326,
    resolution=0.0001
).squeeze("time")

red  = stack.sel(band="B04").astype("float32").rio.write_crs("EPSG:4326")
nir  = stack.sel(band="B08").astype("float32").rio.write_crs("EPSG:4326")
swir = stack.sel(band="B11").astype("float32").rio.write_crs("EPSG:4326")

# 4) Clip to AOI
red  = red.rio.clip([geom], "EPSG:4326", drop=True)
nir  = nir.rio.clip([geom], "EPSG:4326", drop=True)
swir = swir.rio.clip([geom], "EPSG:4326", drop=True)

# 5) NDVI + NDWI
ndvi = (nir - red) / (nir + red + 1e-10)
ndwi = (nir - swir) / (nir + swir + 1e-10)

# 6) Save
ndvi.rio.to_raster("outputs/ndvi.tif")
ndwi.rio.to_raster("outputs/ndwi.tif")

print("Saved ✅ outputs/ndvi.tif and outputs/ndwi.tif")
