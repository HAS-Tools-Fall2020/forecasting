# %%
# Patrick Neri week 10
# Note this is just the code to produce the map, modelling was done using
# previous weeks python scripts.
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
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
filename = 'gagesII_9322_sept30_2011.shp'
filepath = os.path.join('data\Week10', filename)
print(os.getcwd())
print(filepath)
gages = gpd.read_file(filepath)

# %%
# Now lets make a map!
fig, ax = plt.subplots(figsize=(5, 5))
gages.plot(ax=ax)
plt.show()

# Zoom  in and just look at AZ
gages_AZ = gages[gages['STATE'] =='AZ']

# Basic plot of AZ gages
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(ax=ax)
plt.show()

# More advanced - color by attribute
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='OrRd',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()


# %%
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado
filename2 = 'WBD_15_HU2_GDB.gdb'
filepath2 = os.path.join('data\Week10', filename2)
print(os.getcwd())
print(filepath2)
fiona.listlayers(filepath2)
HUC6 = gpd.read_file(filepath2, layer="WBDHU6")

# plot the new layer we got:
fig, ax = plt.subplots(figsize=(5, 5))
HUC6.plot(ax=ax)
ax.set_title("HUC Boundaries")
plt.show()

HUC6.crs

# %%
# Add some points
# UA:  32.22877495, -110.97688412
# STream gauge:  34.44833333, -111.7891667
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])

# make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

# mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)

# plot these on the first dataset
# Then we can plot just one layer at atime
fig, ax = plt.subplots(figsize=(5, 5))
HUC6.plot(ax=ax)
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
plt.show()


# %%
# To fix this we need to re-project
points_project = point_df.to_crs(gages_AZ.crs)

# Project the basins
HUC6_project = HUC6.to_crs(gages_AZ.crs)

# Adding a basemap
# ITS BEAUTIFUL
fig, ax = plt.subplots(figsize=(8, 10))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=80, cmap='OrRd',
              ax=ax)
points_project.plot(ax=ax, color='red', marker='*', markersize=100)
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1)
ctx.add_basemap(ax, crs=gages.crs)
ax.set_title("Stream gages relative to HUC Boundaries")
ax.set(ylim=[1000000, 1450000], xlim=[-1550000, -1300000])

# %%
