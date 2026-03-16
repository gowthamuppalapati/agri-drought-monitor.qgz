import rioxarray as rxr
import numpy as np

d = rxr.open_rasterio("outputs/drought_stress.tif").squeeze()

print("Min:", float(np.nanmin(d)))
print("Max:", float(np.nanmax(d)))
