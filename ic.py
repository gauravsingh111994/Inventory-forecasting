import pandas as pd

read=pd.read_csv("mapping.csv")
read1=pd.read_csv("new.csv")

pd.merge(read,read1,on='PID')
print (read)