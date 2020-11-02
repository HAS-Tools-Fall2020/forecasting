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

# Dataset 1: Basin Boundaries in Shapefile
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
fig.savefig()


# %%


# Let look at what this is
type(gages)
gages.head()
gages.columns
gages.shape

# Looking at the geometry now
gages.geom_type
# check our CRS - coordinate reference system
gages.crs
# Check the spatial extent
gages.total_bounds
# The reference system is different for each dataset. They will be projected.

points_project = point_df.to_crs(gages_AZ.crs)

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
ax.set_title('Prueba')
plt.show()

fig, ax = plt.subplots(figsize=(5, 5))
boundaries.plot(ax=ax)
plt.show()

fig, ax = plt.subplots(figsize=(5, 5))
rivers.plot(ax=ax)
plt.show()


# More advanced - color by attribute
#fig, ax = plt.subplots(figsize=(5, 5))
# gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
#              legend=True, markersize=45, cmap='OrRd',
#              ax=ax)
#ax.set_title("Arizona stream gauge drainge area\n (sq km)")
# plt.show()


# %%
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado
file = os.path.join('../../../data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")

type(HUC6)
HUC6.head()

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
# Now trying to put it all together - adding our two points to the stream gagees
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
point_df.plot(ax=ax, color='r', marker='*')

# Trouble!! we are in two differnt CRS
gages_AZ.crs
point_df.crs

# To fix this we need to re-project
points_project = point_df.to_crs(gages_AZ.crs)

# Trying to plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='r', marker='*')
# NOTE: .to_crs() will only work if your original spatial object has a CRS assigned
# to it AND if that CRS is the correct CRS!

# now putting everythign on the plot:
# Project the basins
HUC6_project = HUC6.to_crs(gages_AZ.crs)

# Now plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1)


# Adding a basemap

fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1)
ctx.add_basemap(ax)
