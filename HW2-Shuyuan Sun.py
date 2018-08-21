
# coding: utf-8

# **NYC Restaurants**
# 
# Setup

# In[1]:


cd C:\Users\ayuan\OneDrive\Documents\2. UT Summer\2.MIS Data Analytics Programming\Assignments


# In[2]:


from pandas import Series, DataFrame
import pandas as pd
get_ipython().magic(u'pylab inline')
df = pd.read_csv('NYC_Restaurants.csv', dtype=unicode)


# [Q1, 6 points] Create a unique name for each restaurant.

# In[3]:


df['RESTAURANT']=df['DBA']+' '+df['BUILDING']+' '+df['STREET']+' '+df['ZIPCODE']
df['RESTAURANT'][:10]


# [Q2, 6 points] How many restaurants are included in the data?

# In[4]:


df_dedup = df.drop_duplicates(subset='RESTAURANT')
print len(df_dedup),'restaurants are included in the data.'


# [Q3, 6 points] How many chains are there?

# In[5]:


restaurant_count=df_dedup['DBA'].value_counts()
restaurant_count
chains_count=restaurant_count[(restaurant_count.values>=2)]
chains_count
print len(chains_count),'chains are included in the data.'


# [Q4, 6 points] Plot a bar graph of the top 20 most popular chains.

# In[6]:


top_20_chains = chains_count[:20]
top_20_chains.plot(kind='bar')


# [Q5, 6 points] What fraction of all restaurants are chains?

# In[7]:


chains_sum=chains_count.sum()
chains_fraction=1.0*chains_sum/len(df_dedup)
print chains_fraction*100,'% of all restaurants are chains.'


# [Q6, 6 points] Plot the number of non-chain restaurants in each boro.

# In[8]:


non_chains_count=restaurant_count[(restaurant_count.values<2)]
non_chains_count
def non_chain(x):
    return (x in non_chains_count.index)
mask_non_chains = (df_dedup['DBA'].map(non_chain))
df_non_chains=df_dedup[mask_non_chains]
mask_missing= (df_non_chains['BORO'] == 'Missing')
df_non_chains.loc[mask_missing,'BORO'] = np.nan
df_non_chains['BORO'].value_counts().plot(kind='bar')


# [Q7, 8 points] Plot the fraction of non-chain restaurants in each boro.

# In[9]:


mask_missing_= (df_dedup['BORO'] == 'Missing')
df_dedup.loc[mask_missing_,'BORO'] = np.nan
res_per_boro=df_dedup['BORO'].value_counts()
nonchains_per_boro=df_non_chains['BORO'].value_counts()
nonchains_frac=1.0*nonchains_per_boro/res_per_boro
nonchains_frac_rank=nonchains_frac.sort_values(ascending=False)
nonchains_frac_rank.plot(kind='bar')
#Is the boro with the most independent restaurants also the one with the highest ratio of independent restaurants?
#No. Manhattan has the most independent restaurants, but Brooklyn has the highest ratio of independent restaurants.


# [Q8, 6 points] Plot the popularity of cuisines.

# In[10]:


cuisine_count=df_dedup['CUISINE DESCRIPTION'].value_counts()
cuisine_count[:20].plot(kind='bar')


# [Q9, 9 points] Plot the cuisines among restaurants which never got cited for violations.

# In[11]:


mask_violation=(df['VIOLATION CODE'].isnull()==False)
df_vio=df[mask_violation]
rest_vio=list(df_vio['RESTAURANT'])
df_nonvio=df_dedup[~df_dedup.RESTAURANT.isin(rest_vio)]
nonvio_cuisine_count=df_nonvio['CUISINE DESCRIPTION'].value_counts()
nonvio_cuisine_count[:20].plot(kind='bar')


# [Q10, 6 points] What cuisines tend to be the \cleanest"?

# In[12]:


mask_clean=(cuisine_count.values>=20)
over20_cuisine_count=cuisine_count[mask_clean]
cuisine_clean_ratio=(1.0*nonvio_cuisine_count/over20_cuisine_count).dropna()
cuisine_clean_ratio=cuisine_clean_ratio.sort_values(ascending=False)
cuisine_clean_ratio[:10]


# [Q11, 8 points] What are the most common violations in each borough?

# In[13]:


mask_missing__= (df['BORO'] == 'Missing')
df.loc[mask_missing__,'BORO'] = np.nan
violation_boro= pd.crosstab(df['VIOLATION DESCRIPTION'], df['BORO'])
violation_boro.idxmax()


# [Q12, 9 points] What are the most common violations per borough, after normalizing for the relative abundance of each violation?

# In[14]:


violationFrequency=df['VIOLATION DESCRIPTION'].value_counts()
vio_normalize=1.0*violation_boro.T/violationFrequency
vio_normalize.T.idxmax()


# [Q13, 8 points] How many phone area codes correspond to a single zipcode? 

# In[15]:


df['AREACODE']=df['PHONE'].str[:3]
df_dedup['AREACODE']=df_dedup['PHONE'].str[:3]
df_areacode_zip=df[['AREACODE','ZIPCODE']]
df_areacode_zip=df_areacode_zip.drop_duplicates(subset=['AREACODE','ZIPCODE'])
areacode_zip_count=df_areacode_zip['AREACODE'].value_counts()
mask_areacode=(areacode_zip_count==1)
ac_zip_single=areacode_zip_count[mask_areacode]
print len(ac_zip_single),'phone area codes correspond to a single zipcode.'


# [Q14, 10 points] Find common misspellings of street names

# In[16]:


#STREET TYPE
street_split=df_dedup['STREET'].str.split()
street_split_dict=dict(street_split)
street_type_dict={}
for i in street_split_dict:
    street_type_dict[i]=street_split_dict[i][-1]
street_type=pd.Series(street_type_dict)
df_dedup['STREET TYPE']=street_type


# In[17]:


#STREET BASE
street_base_dict={}
for m in street_split_dict:
    if len(street_split_dict[m][:-1])>0:
        street_base_dict[m]=street_split_dict[m][:-1]
        street_base_dict[m]=''.join(street_base_dict[m])
street_base=pd.Series(street_base_dict)
df_dedup['STREET BASE']=street_base.dropna()


# In[18]:


#STREET BASE & ZIP
df_dedup['STREET BASE & ZIP']=df_dedup['STREET BASE']+' '+df_dedup['ZIPCODE']


# In[19]:


#Create a table
table=DataFrame([df_dedup['STREET TYPE'],df_dedup['STREET BASE'],df_dedup['STREET BASE & ZIP']])
st_table=table.T
st_table=st_table.drop_duplicates(subset=['STREET TYPE','STREET BASE','STREET BASE & ZIP'])
st_table1=st_table.dropna()


# In[20]:


#Merge the table
st_table_square= st_table1.merge(st_table1,
                                   left_on=['STREET BASE & ZIP','STREET BASE'],
                                   right_on=['STREET BASE & ZIP','STREET BASE'],
                                   suffixes=['_1', '_2'])


# In[21]:


#Different st.type
st_table_dif=st_table_square.loc[(st_table_square['STREET TYPE_1']!=st_table_square['STREET TYPE_2'])]


# In[22]:


#Cross-tabulation
st_cross=pd.crosstab(st_table_dif['STREET TYPE_1'], st_table_dif['STREET TYPE_2'])


# In[23]:


#Most commonly street type
max_table=st_cross.idxmax()
max_table.loc[['AVE','ST', 'RD', 'PL', 'BOULEARD','BULEVARD']]

