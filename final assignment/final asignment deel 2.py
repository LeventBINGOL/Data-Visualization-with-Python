#!/usr/bin/env python
# coding: utf-8

# In[137]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[2]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# In[138]:


df_sanfran = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')


# In[139]:


df_sanfran.head()


# In[111]:


df_sanfran.tail()


# In[112]:


df_sanfran.info()


# In[113]:


df_sanfran.columns.values, df_sanfran.index.values 


# In[117]:


df_sanfran ['Category']


# In[35]:


df_sanfran.columns.tolist()


# In[125]:


df_sanfran.shape
df_sanfran.columns.values


# In[118]:


df_sanfran.rename(columns={"PdDistrict":"Neighborhood"},inplace=True)
df_sanfran.rename(columns={"IncidntNum":"Count"},inplace=True)


# In[132]:


df_ng=df_sanfran [['Neighborhood',"Count"]]
df_ng


# In[133]:


df_ng=df_ng.groupby("Neighborhood",axis=0).count()


# In[134]:


df_ng


# In[135]:


df_ng.reset_index(inplace=True)


# In[136]:



df_ng


# In[169]:



df_ng


# In[84]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# In[175]:


#df_ng['Count'].min(), df_ng['Count'].max()
#df_ng.info()
#df_ng['Neighborhood']
# for sake of consistency, let's also make all column labels of type string
df_ng.columns = list(map(str, df_ng.columns))


# In[176]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)


# In[178]:


sanfran_geo = r'san-francisco.geojson'

# create a numpy array of length 6
threshold_scale = np.linspace(df_ng['Count'].min(),
                              df_ng['Count'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1 # make sure that the last value of the list is greater than the maximum immigration

# let Folium determine the scale.
#sanfran_map = folium.Map(location=[0, 0], zoom_start=2, tiles='Mapbox Bright')
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

sanfran_map.choropleth(
    geo_data=sanfran_geo,
    data=df_ng,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    threshold_scale=threshold_scale,
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco',
    reset=True
)
sanfran_map


# In[ ]:





# In[ ]:




