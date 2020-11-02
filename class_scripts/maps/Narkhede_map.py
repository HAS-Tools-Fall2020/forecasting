# %%
# %%
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%

#  1. Streamgauges: Gauges II USGS stream gauge dataset
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('data/gagesII_9322_point_shapefile',
                    'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Exploring
gages.columns
gages.shape

# Looking at the geometry now
gages.geom_type
# check our CRS - coordinate reference system
gages.crs
# Check the spatial extent
gages.total_bounds
gages.describe

# %%
# Now lets make a map!
fig, ax = plt.subplots(figsize=(5, 5))
gages.plot(ax=ax)
plt.show()

# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_AZ = gages[gages['STATE'] == 'AZ']
gages_AZ.shape

# Basic plot of AZ gages
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(ax=ax)
plt.show()

# More advanced - color by attribute
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, marker='^', markersize=45, cmap='viridis',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()

# %%
# 2. Watershed: Boundaries for Lower Colorado basin
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Watershed boundaries for the lower colorado
file = os.path.join('data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")

type(HUC6)
HUC6.head()

# %%
# Adding Verde River Stream gauge
verde_gage = gages_AZ[gages_AZ['STAID'] ==
                      '09506000'][['LAT_GAGE', 'LNG_GAGE']]
point_list = np.array([[-111.789871, 34.448361]])

# make these into spatial features
point_geom = [Point(xy) for xy in point_list]

# mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)

# plot these on the first dataset
fig, ax = plt.subplots(figsize=(8, 8))
HUC6.plot(ax=ax, edgecolor='k', facecolor='cyan')
point_df.plot(ax=ax, color='red', marker='s', markersize=30)
ax.set_title("HUC Boundaries")
plt.show()

# %%
# 3. Arizona state boundaries
# https://www.sciencebase.gov/catalog/item/59fa9f59e4b0531197affb13

filepath2 = os.path.join('data/State_bnd', 'GU_StateOrTerritory.shp')
fiona.listlayers(filepath2)
state = gpd.read_file(filepath2)

state.type
state.head()
state_AZ = state[state['State_Name'] == 'Arizona'][['geometry']]
state_df = gpd.GeoDataFrame(state_AZ, columns=['geometry'],
                            crs=HUC6.crs)

# plot of Arizona state boundaries
fig, ax = plt.subplots(figsize=(8, 8))
state_df.plot(ax=ax, color='none', edgecolor='Red')
ax.set_title("Arizona boundaries")
plt.show()
state.crs

# 4. Lakes in Arizona state

filepath4 = os.path.join('data/Lakes', 'hydrography_p_lakes_v2.shp')
print(os.getcwd())
print(filepath4)
os.path.exists(filepath4)
lakes = gpd.read_file(filepath4)

lakes.columns
lakes.shape

lakes.crs
lake_data = gpd.GeoDataFrame(lakes, crs=HUC6.crs)
lake_data = lake_data.to_crs(HUC6.crs)
US_lakes = lake_data[lake_data['COUNTRY'] == 'USA']
Lake_Mead = US_lakes[US_lakes['NAMEEN'] == 'Lake Mead']
lake_project = Lake_Mead.to_crs(gages_AZ.crs)
fig, ax = plt.subplots(figsize=(5, 5))
lake_project.plot(ax=ax, color='Red')

# %%
# Plotting everything together

# Re-projecting Verde gage
points_project = point_df.to_crs(gages_AZ.crs)

# Plotting gages and Verde gage
fig, ax = plt.subplots(figsize=(8, 8))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, marker='^', markersize=45, cmap='viridis',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
points_project.plot(ax=ax, color='r', marker='s', markersize=35)

HUC6_project = HUC6.to_crs(gages_AZ.crs)

State_bnd = state_df.to_crs(gages_AZ.crs)

fig, ax = plt.subplots(figsize=(8, 8))
State_bnd.plot(ax=ax, color='none', edgecolor='Red')
ax.set_title("Arizona boundaries")
plt.show()
# %%

# Plotting final all in one
fig, ax = plt.subplots(figsize=(8, 8))
HUC6_project.plot(ax=ax, edgecolor='black', alpha=0.5,
                  facecolor='cyan', legend=True)
lake_project.plot(ax=ax, color='blue', edgecolor='magenta', linewidth=4)
State_bnd.plot(ax=ax, color='yellow', alpha=0.5, edgecolor='r', linewidth=2)
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, marker='^', markersize=30, cmap='viridis',
              ax=ax)
points_project.plot(ax=ax, color='r', marker='s', markersize=45)
ctx.add_basemap(ax)
ax.set_title("Stream guages in Arizona in lower Colorado basin")
ax.legend(['Stream guages', 'Verde River guage'])
plt.show()
fig.savefig("Map.png")

# %%
