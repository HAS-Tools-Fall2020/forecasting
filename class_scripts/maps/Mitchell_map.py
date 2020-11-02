# Mapping Start
# By Benjamin Mitchell

# %%
# Import the modules we will use
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import os
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
from pprint import pprint

# %%
# 1) Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('../../../HAS-Tools-Fall2020_local/USGS/gagesII_9322_point_shapefile',
                    'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Zoom  in and just look at AZ
# gages.columns
# gages.STATE.unique()
gages_az=gages[gages['STATE']=='AZ']
# gages_az.shape


# %%
# 2) USDA Forest Service for the National Forests:
# Download here:
# https://www.fs.usda.gov/coronado
# https://data.fs.usda.gov/geodata/edw/datasets.php

# Reading it using geopandas
file = os.path.join('../../../HAS-Tools-Fall2020_local/USDA_Forest_Service/S_USA.AdministrativeForest',
                    'S_USA.AdministrativeForest.shp')
forest = gpd.read_file(file)
# print(forest.head())

forests_az = ['Kaibab National Forest', 'Prescott National Forest',
              'Coconino National Forest', 'Tonto National Forest',
              'Apache-Sitgreaves National Forests', 'Coronado National Forest']
forest_az=forest[forest['FORESTNAME'].isin(forests_az)]
# forest_az.shape
# print(forest_az.head())


# %%
# 3) The State of Arizona
# Download here:
# https://repository.arizona.edu/handle/10150/188734

file = os.path.join('../../../HAS-Tools-Fall2020_local/DataGov/tl_2016_04_cousub',
                    'tl_2016_04_cousub.shp')
fiona.listlayers(file)
az = gpd.read_file(file)
# az.shape
# print(az.head())


# %%
# 4) WBD 20201002 for AZ
# Download here:
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado 
file = os.path.join('../../../HAS-Tools-Fall2020_local/USGS/WBD_15_HU2_GDB',
                    'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")


# %%
# 5) Add some important points
# UA:  32.22877495, -110.97688412
# Stream gauge:  34.44833333, -111.7891667
UofA_np = np.array([[-110.97688412, 32.22877495]])

Gage_np = np.array([[-111.7891667, 34.44833333]])

#make these into spatial features
UofA_geom = [Point(xy) for xy in UofA_np]
Gage_geom = [Point(xy) for xy in Gage_np]
UofA_geom
Gage_geom

#mape a dataframe of these points
UofA = gpd.GeoDataFrame(UofA_geom, columns= ['geometry'],
                        crs=HUC6.crs)

Gage = gpd.GeoDataFrame(Gage_geom, columns= ['geometry'],
                        crs=HUC6.crs)


# %%
# To fix this we need to re-project
forest_az_proj = forest_az.to_crs(gages_az.crs)
HUC6_proj = HUC6.to_crs(gages_az.crs)
az_proj = az.to_crs(gages.crs)
UofA_proj = UofA.to_crs(gages_az.crs)
Gage_proj = Gage.to_crs(gages_az.crs)


# %%
# Time to Plot
fig, ax = plt.subplots(figsize=(10, 10))
gages_az.plot(ax=ax, label='All Stream Gages', color='cyan', markersize=10,
              zorder=3)
forest_az_proj.boundary.plot(ax=ax, label='National Forest Bounds',
                             facecolor='darkgreen', edgecolor='blue',
                             linewidth=1, zorder=2)
HUC6_proj.boundary.plot(ax=ax, label='HUC6 Bonds', color=None,
                        edgecolor='black', linewidth=0.5, zorder=1)
az_proj.plot(ax=ax, label='Arizona', color='grey', zorder=0)
UofA_proj.plot(ax=ax, label='U of A', color='red', edgecolor='blue', marker='^',
               markersize=250, zorder=4)
Gage_proj.plot(ax=ax, label='Gage# 09506000', color='orange', edgecolor='blue', marker='*',
               markersize=700, zorder=5)
ax.set_title('Arizona National Forests w/ Stream Gages')
ax.set_xlabel('Long')
ax.set_ylabel('Lat')
ax.legend()
plt.show()

fig.savefig("graphs/Arizona_National_Forests_w_Stream_Gages.png")



# %%
