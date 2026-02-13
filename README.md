🌱 Satellite-Based Drought Stress and Irrigation Priority Mapping


📌 Project Overview
This project demonstrates a remote sensing workflow for agricultural drought monitoring using open satellite data and Python. Sentinel-2 imagery is used to derive vegetation and water indices, which are combined to detect drought stress and generate irrigation priority zones.
The workflow provides a simple decision-support tool for precision agriculture and sustainable water management.


🎯 Objectives
Monitor vegetation health using satellite imagery
Detect crop water stress
Identify drought-affected zones
Generate irrigation priority maps

🛰️ Data Sources
Sentinel-2 Level-2A imagery
Planetary Computer STAC API

📊 Methodology
Area of Interest (AOI) creation in QGIS
Satellite data acquisition using STAC API
NDVI calculation (vegetation health)
NDWI calculation (vegetation water content)
Drought stress index generation
Classification into irrigation priority zones

📁 Outputs

NDVI map
NDWI map
Drought stress map
Irrigation priority map

🛠 Tools & Technologies
Python
GeoPandas
Rasterio & Rioxarray
Stackstac

QGIS
Sentinel-2 satellite data

📈 Results
The model successfully identifies spatial variability in vegetation health and drought stress and converts it into actionable irrigation priority zones.

Digital farming systems

Agricultural monitoring
