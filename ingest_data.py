#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__file__


# In[3]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
df = pd.read_csv(url)

# Display first rows
df.head()

# Check data types
df.dtypes

# Check data shape
df.shape


# In[4]:


df.head()


# In[5]:


len(df)


# In[6]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    # nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[7]:


df.head()


# In[11]:


df.tpep_pickup_datetime.dtype


# In[11]:


get_ipython().system('uv add sqlalchemy psycopg2-binary')


# In[12]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[14]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[15]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[16]:


len(df)


# In[17]:


df_iter=pd.read_csv(
    url, 
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000,
)



# In[18]:


df=next(df_iter)


# In[19]:


df


# In[20]:


get_ipython().system(' uv add tqdm')


# In[22]:


from tqdm.auto import tqdm


# In[26]:


# total_rows = sum(1 for _ in open('your_file.csv')) - 1  # minus header
total_rows = len(df)
chunksize = 100000
total_chunks = total_rows // chunksize + 1
df_iter = pd.read_csv(url, chunksize=chunksize)

for df_chunk in tqdm(df_iter, total=total_chunks):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')



# In[27]:


len(df)


# In[30]:


total_rows = pd.read_csv(url, usecols=[0]).shape[0]
print(total_rows)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




