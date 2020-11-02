# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
import os
from shapely.geometry import Point

# %%

# Use this link to download the stream segments that make up AZ nations surface
# water discharge system https://www.sciencebase.gov/catalog/item/5a96cda0e4b06990606c4d0f
# Be sure to update your folder name, it is in a folder called "data-nongit" on my 
# local drive.

file = os.path.join('data-nongit', 'NHD_H_Arizona_State_GDB.gdb')
fiona.listlayers(file)
HUC4 = gpd.read_file(file, layer="WBDHU4")
NHDArea = gpd.read_file(file, layer="NHDArea")
NHDLine = gpd.read_file(file, layer="NHDLine")

# Adding in some points of interest: Stream gauge location and 
# beginning of Verde River

point_list = np.array([[-112.45172, 34.8559],
                       [-111.7891667, 34.44833333]])

# Making into spatial features
point_geom = [Point(xy) for xy in point_list]
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC4.crs)

# Plotting all the layers together
fig, ax = plt.subplots(figsize=(5, 5))
HUC4.boundary.plot(ax=ax, color = None, label = "HUC4")
point_df.plot(ax=ax, color='darkgreen', marker='X', label = "Stream Gauges")
NHDArea.plot(ax=ax, color = "black", label = "NHD Area")
NHDLine.plot(ax=ax, color = 'red', label= "NHD Line")
ax.set_title("4 layers")
ax.legend()
plt.show()

# %%