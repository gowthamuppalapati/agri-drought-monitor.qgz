import rioxarray as rxr
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. Load NDVI and NDWI
# -------------------------
ndvi = rxr.open_rasterio("outputs/ndvi.tif").squeeze()
ndwi = rxr.open_rasterio("outputs/ndwi.tif").squeeze()

print("NDVI and NDWI loaded ✅")

# -------------------------
# 2. Normalize (0–1 range)
# -------------------------
def normalize(x):
    return (x - np.nanmin(x)) / (np.nanmax(x) - np.nanmin(x) + 1e-10)

ndvi_n = normalize(ndvi)
ndwi_n = normalize(ndwi)

print("Normalization complete ✅")

# -------------------------
# 3. Compute drought stress
# -------------------------
drought = 1 - ((ndvi_n + ndwi_n) / 2)

drought = drought.rio.write_crs(ndvi.rio.crs)

print("Drought stress calculated ✅")

# -------------------------
# 4. Save result
# -------------------------
output_path = "outputs/drought_stress.tif"
drought.rio.to_raster(output_path)

print("Saved:", output_path)

# -------------------------
# 5. Preview
# -------------------------
plt.figure()
drought.plot(cmap="RdYlGn_r")
plt.title("Drought Stress Map")
plt.show()
