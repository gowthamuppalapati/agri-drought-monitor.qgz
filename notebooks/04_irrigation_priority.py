import rioxarray as rxr
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. Load drought stress map
# -------------------------
drought = rxr.open_rasterio(
    "outputs/drought_stress.tif"
).squeeze()

print("Drought map loaded ✅")

# -------------------------
# 2. Create irrigation classes
# -------------------------
# 0 = No irrigation
# 1 = Monitor
# 2 = Irrigate first

priority = np.zeros_like(drought)

priority = np.where(drought > 0.6, 2, priority)
priority = np.where((drought > 0.4) & (drought <= 0.6), 1, priority)

priority = priority.astype("int16")

priority = drought.copy(data=priority)

print("Priority zones created ✅")

# -------------------------
# 3. Save output
# -------------------------
output_path = "outputs/irrigation_priority.tif"
priority.rio.to_raster(output_path)

print("Saved:", output_path)

# -------------------------
# 4. Preview
# -------------------------
plt.figure()
priority.plot(cmap="RdYlGn_r")
plt.title("Irrigation Priority Zones")
plt.show()
