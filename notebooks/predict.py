import pickle
import numpy as np
import pandas as pd
from sys import argv

columns = ['cement','blast_furnace_slag','fly_ash','water','superplasticizer','coarse_aggregate','fine_aggregate','age']
data_dictionary = {}
for col in columns:
    data_index = argv.index(col) + 1
    data_dictionary[col] = [argv[data_index]]

#Loading the model
with open('notebooks/models/model.pkl','rb') as file:
    model = pickle.load(file)

df = pd.DataFrame(data=data_dictionary,
             columns=columns)
df.rename({'fine_aggregate' : 'fine_aggregate '},axis = 1,inplace=True)
pred = (model.predict(df)[0])
print(f"The Concrete compressive strength is {pred}")