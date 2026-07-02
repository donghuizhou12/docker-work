import sys
import pandas as pd
import os
print("cwd:", os.getcwd())
df=pd.DataFrame({'Day':[1,2,3,5,6,7],'num_passenger':[4,5,6,7,8,9]})
print(df.head() )
print('arguments:', sys.argv)
month=int(sys.argv[1])
df.to_parquet(f'output_{month}.parquet')
print(f'hello pipeline , month ={month} ')