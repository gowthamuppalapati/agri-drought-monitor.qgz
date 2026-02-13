import geopandas as gpd

aoi = gpd.read_file("data/aoi.geojson")
print("AOI loaded ✅")
print("CRS:", aoi.crs)
print("Bounds:", aoi.total_bounds)
