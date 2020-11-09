# %%
# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx


# %%
# Upload the datasets used in the map

# Dataset 1: Gages in Shapefile
# Download at: https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

file_name = '02_Mapping/Definitive/gages/gagesII_9322_sept30_2011.shp'
file_boundaries = os.path.join('../../../../', file_name)
gages = gpd.read_file(file_boundaries)

# %%
# Dateset 2: Rivers and Streams at US
# Download at: https://hub.arcgis.com/datasets/esri::usa-rivers-and-streams
file_rivers_name = '02_Mapping/Definitive/USA_Rivers/riversshape.shp'
file_rivers = os.path.join('../../../../', file_rivers_name)
rivers = gpd.read_file(file_rivers)

# %%
# Dataset 3: Basin boundaries in the US
# Download at: https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View
file_boundaries_name = '02_Mapping/Definitive/basin/basin.shp'
file_boundaries = os.path.join('../../../..', file_boundaries_name)
boundaries = gpd.read_file(file_boundaries)
# %%
# Information Preparation
# Extract the gauges from Arizona
gages_AZ = gages[gages['STATE'] == 'AZ']
AZ_rivers = rivers.loc[rivers['Name'] == 'Verde River']

# Validate the reference system
print('Gauges:', gages.crs)
print('Basins:', boundaries.crs)
print('Rivers:', rivers.crs)

# The reference system is different for each dataset. They will be projected.

basins_project = boundaries.to_crs(gages_AZ.crs)
rivers_project = AZ_rivers.to_crs(gages_AZ.crs)

# %%
# Plotting the map

# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_AZ = gages[gages['STATE'] == 'AZ']
gages_AZ.shape

# Plotting
fig, ax = plt.subplots(figsize=(5, 10))

ax.set_title('Verde River Basin', fontsize=15)

basins_project.plot(ax=ax, label='Basins',
                    edgecolor='black', alpha=0.3, legend=True)
gages_AZ.plot(ax=ax, label='Gauges', marker='*', color='green')
rivers_project.plot(ax=ax, label='Verde River', color='blue')
ax.legend()
ctx.add_basemap(ax)

plt.show()
fig.savefig('Salcedo_map.png')


# %%
