# %% 
# HW 10 - Richard Marcelain
# Create a map with 4 layers (incl. 2 vectors) with a legend

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
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('E://datasets//gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Let look at what this is 
type(gages)
gages.head()
gages.columns
gages.shape

# Looking at the geometry now
gages.geom_type
#check our CRS - coordinate reference system 
gages.crs
#Check the spatial extent 
gages.total_bounds
#NOTE to selves - find out how to get these all at once

# %% 
# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_az=gages[gages['STATE']=='AZ']
gages_az.shape

# AZ Gages - color by attribute
fig, ax = plt.subplots(figsize=(5, 5))
gages_az.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='RdBu',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()


# %% 
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado 
file = os.path.join('E://datasets//WBD_15_HU2_GDB.gdb')

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
# Add data points
ua_np = np.array([[-110.97688412, 32.22877495]])
verde_np = np.array([[-111.7891667, 34.44833333]])

# Make these into spatial features
ua_geom = [Point(xy) for xy in ua_np]
verde_geom = [Point(xy) for xy in verde_np]
ua_geom
verde_geom

# Make a dataframe of these points
ua = gpd.GeoDataFrame(ua_geom, columns= ['geometry'],
                        crs=HUC6.crs)

verde = gpd.GeoDataFrame(verde_geom, columns= ['geometry'],
                        crs=HUC6.crs)

# Re-project onto map
ua_point = ua.to_crs(gages_az.crs)
verde_point = verde.to_crs(gages_az.crs)


# %%
# Rivers layer
# https://repository.arizona.edu/handle/10150/188710
file = os.path.join('E://datasets//az_hydro_routesNAD83.shp')
fiona.listlayers(file)
az_rivers = gpd.read_file(file)
az_proj_rivers = az_rivers.to_crs(gages.crs)


# %% 
# Project the basins 
HUC6_project = HUC6.to_crs(gages_az.crs)


# Plot
fig, ax = plt.subplots(figsize=(10, 10))
gages_az.plot(ax=ax, label='All Stream Gages', color='blue', markersize=10,
              zorder=3)
HUC6_project.boundary.plot(ax=ax, label='HUC6 Bondary', color=None,
                        edgecolor='black', linewidth=0.8, zorder=2)
az_proj_rivers.plot(ax=ax, label='Rivers', color='grey', zorder=0)
ua_point.plot(ax=ax, label='UA Gage', color='red', edgecolor='white', marker='v',
               markersize=150, zorder=4)
verde_point.plot(ax=ax, label='Verde River Gage', color='orange', edgecolor='white', marker='v',
               markersize=150, zorder=5)
ax.set_title('Arizona Stream Gages')
ax.set_xlabel('Northing (m)')
ax.set_ylabel('Easting (m)')
ctx.add_basemap(ax, crs=gages_az.crs, url=ctx.providers.OpenTopoMap, zorder=1, alpha=0.5)
ax.legend()
plt.show()
fig.savefig("map.png")
# 


# %%
