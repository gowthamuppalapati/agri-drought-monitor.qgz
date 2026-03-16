import rioxarray as rxr
import numpy as np

# Load drought map
drought = rxr.open_rasterio("outputs/drought_stress.tif").squeeze()

# Print stats (so we know it’s not empty)
print("Drought stats ✅")
print("Min:", float(np.nanmin(drought)))
print("Max:", float(np.nanmax(drought)))

# Thresholds based on your data distribution
low = float(np.nanpercentile(drought, 33))
high = float(np.nanpercentile(drought, 66))

print("Low threshold (33%):", low)
print("High threshold (66%):", high)

# Class map: 0=no irrigation, 1=monitor, 2=irrigate first
priority = np.zeros_like(drought, dtype="int16")
priority = np.where(drought >= high, 2, priority)
priority = np.where((drought >= low) & (drought < high), 1, priority)

# Wrap back into xarray with same geo info
priority_xr = drought.copy(data=priority)

# Save
out_path = "outputs/irrigation_priority.tif"
priority_xr.rio.to_raster(out_path)

print("Saved ✅", out_path)

# Quick count of pixels in each class (super useful)
unique, counts = np.unique(priority[~np.isnan(priority)], return_counts=True)
print("Class counts:", dict(zip(unique.tolist(), counts.tolist())))
