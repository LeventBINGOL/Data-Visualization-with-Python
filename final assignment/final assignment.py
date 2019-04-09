#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[16]:


df_survey = pd.read_csv('Topic_Survey_Assignment.csv')


# In[17]:


df_survey.head()


# In[18]:


# print the dimensions of the dataframe
print(df_survey.shape)


# In[19]:


df_survey.rename(columns={'Unnamed: 0':' '}, inplace=True)


# In[20]:


df_survey.head()


# In[21]:


df_survey.set_index(' ', inplace=True)


# In[22]:


df_survey


# In[14]:


values= df_survey.sort_values(['Very interested'], ascending= False, axis=0,inplace=True)


# In[17]:


df_survey


# In[16]:


df_survey[:]=df_survey[:]/2233


# In[18]:


df_survey=round(df_survey,2)
#df_survey=df_survey.transpose()


# In[19]:


df_survey


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt

#mpl.style.use('ggplot') # optional: for ggplot-like style

# check for latest version of Matplotlib
#print('Matplotlib version: ', mpl.__version__) # >= 2.0.0



# In[31]:


#MASTER ANSWER LEVENT
#df_iceland.plot(kind='bar', figsize=(10, 6), rot=90) 
colors=('#5cb85c ','#5bc0de','#d9534f')
ax = df_survey.plot(kind='bar',figsize=(20, 8),rot=90,width=0.8, color=('#5cb85c','#5bc0de','#d9534f'), fontsize=14)
ax.set_title("Percentage of Respondents' Interests in Data Science Areas",fontsize=16)
#ax.set_yticklabels('')
ax.legend(fancybox=True, fontsize=14,facecolor='w',edgecolor='b',loc=0,bbox_to_anchor=(0.5, 0.45, 0.5, 0.5))
ax.set_facecolor('w')

#plt.tick_params(axis='x', which='major', bottom=False)
ax.spines['left'].set_visible(False);
ax.spines['top'].set_visible(False);
ax.spines['right'].set_visible(False);
ax.spines['bottom'].set_color('#CCCCCC');
# Remove axes tick marks:
# . remove both ticks and labels on y-axis
plt.yticks([]);

# Annotate Text
x_offset = 0
y_offset = 0.03
for p in ax.patches:
    p_x = p.get_x()
    p_h = p.get_height()
    ax.text( x=p_x + x_offset, y=p_h + y_offset, 
             #s="{:.0f}%".format(round(p_h, 0)), 
             s="{:.0f}%".format(round(p_h*100, 0)),
             ha='left', va='center', fontsize=12)
plt.savefig('answer2.png')


# In[29]:


import matplotlib.pyplot as plt
# Parameters:
df=df_survey
size = (20, 8)
# bar_width = 0.8 : default
a = 0.8
font_size = 14
colors = ['#5cb85c', '#5bc0de', '#d9534f']
ax = df.plot(kind='bar', color=colors, alpha=a, 
             figsize=size, fontsize=font_size);
# The bars will show the values, so no need for frames
ax.spines['left'].set_visible(False);
ax.spines['top'].set_visible(False);
ax.spines['right'].set_visible(False);
ax.spines['bottom'].set_color('#CCCCCC');
# Remove axes tick marks:
# . remove both ticks and labels on y-axis
plt.yticks([]);
# . remove ticks only on x-axis:
#plt.tick_params(axis='x', which='major', bottom=False)
# Adjust vertical limits to 100% to get more whitespace 
# below the title:
plt.ylim(0, 1)
# Annotate Text
x_offset = 0
y_offset = 0.03
for p in ax.patches:
    p_x = p.get_x()
    p_h = p.get_height()
    ax.text( x=p_x + x_offset, y=p_h + y_offset, 
             #s="{:.0f}%".format(round(p_h, 0)), 
             s="{:.0f}%".format(round(p_h*100, 0)),
             ha='left', va='center', fontsize=12)
        
# NOTE: ha='left' goes with x_offset = 0. If instead, ha='center',
#       the label will 'pre-hang' over the bar, so an x-position
#       offset will be needed; typically x_offset = p.get_width()/2.
# Reset legend font size from smaller default:
plt.legend(fontsize=14);
plt.title("Percentage of Respondents' interest in Data Science Areas", fontsize=16);

plt.show();


# In[29]:


import matplotlib.pyplot as plt
# Parameters:
df=df_survey
size = (20, 8)
# bar_width = 0.8 : default
a = 0.8
font_size = 14
colors = ['#5cb85c', '#5bc0de', '#d9534f']
ax = df.plot(kind='bar', color=colors, alpha=a, 
             figsize=size, fontsize=font_size);
# The bars will show the values, so no need for frames
ax.spines['left'].set_visible(False);
ax.spines['top'].set_visible(False);
ax.spines['right'].set_visible(False);
ax.spines['bottom'].set_color('#CCCCCC');
# Remove axes tick marks:
# . remove both ticks and labels on y-axis
plt.yticks([]);
# . remove ticks only on x-axis:
#plt.tick_params(axis='x', which='major', bottom=False)
# Adjust vertical limits to 100% to get more whitespace 
# below the title:
plt.ylim(0, 1)
# Annotate Text
x_offset = 0
y_offset = 0.03
for p in ax.patches:
    p_x = p.get_x()
    p_h = p.get_height()
    ax.text( x=p_x + x_offset, y=p_h + y_offset, 
             #s="{:.0f}%".format(round(p_h, 0)), 
             s="{:.0f}%".format(round(p_h*100, 0)),
             ha='left', va='center', fontsize=12)
        
# NOTE: ha='left' goes with x_offset = 0. If instead, ha='center',
#       the label will 'pre-hang' over the bar, so an x-position
#       offset will be needed; typically x_offset = p.get_width()/2.
# Reset legend font size from smaller default:
plt.legend(fontsize=14);
plt.title("Percentage of Respondents' interest in Data Science Areas", fontsize=16);

plt.show();


# In[28]:


import matplotlib.pyplot as plt
# Parameters:
df=df_survey
size = (20, 8)
bar_width = 0.8 # default
#a = 0.8
font_size = 14
colors = ['#5cb85c', '#5bc0de', '#d9534f']
ax = df.plot(kind='bar', color=colors, 
             figsize=size, fontsize=font_size);
# The bars will show the values, so no need for frames
ax.spines['left'].set_visible(False);
ax.spines['top'].set_visible(False);
ax.spines['right'].set_visible(False);
ax.spines['bottom'].set_color('#CCCCCC');
# Remove axes tick marks:
# . remove both ticks and labels on y-axis
plt.yticks([]);
# . remove ticks only on x-axis:
plt.tick_params(axis='x', which='major', bottom=False)
# Adjust vertical limits to 100% to get more whitespace 
# below the title:
plt.ylim(0, 1)
# Annotate Text
x_offset = 0
y_offset = 0.03
for p in ax.patches:
    p_x = p.get_x()
    p_h = p.get_height()
    ax.text( x=p_x + x_offset, y=p_h + y_offset, 
             #s="{:.0f}%".format(round(p_h, 0)), 
             s="{:.0f}%".format(round(p_h*100, 0)),
             ha='left', va='center', fontsize=12)
        
# NOTE: ha='left' goes with x_offset = 0. If instead, ha='center',
#       the label will 'pre-hang' over the bar, so an x-position
#       offset will be needed; typically x_offset = p.get_width()/2.
# Reset legend font size from smaller default:
plt.legend(fontsize=14);
plt.title("Percentage of Respondents' interest in Data Science Areas", fontsize=16);

plt.show();


# In[ ]:





# In[ ]:




