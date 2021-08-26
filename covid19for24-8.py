import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os

dataset = gpd.read_file(r'C:\GIS Courses\Arcpy\ksa_Regions Polygon.shp')

ax = dataset.plot(cmap = 'OrRd', column = '24_8_2021', legend = True)

ax.set_title('Daily Report for Coronavirus Disease COVID-19 in 24-8-2021')

ax.set_axis_off()
