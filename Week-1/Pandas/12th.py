import pandas as pd 
import numpy as np 
dict = {'Name': ['Sumit Tyagi', 'Sukritin', 'Akriti Goel', 
				'Sanskriti', 'Abhishek Jain'], 
		'Age': [22, 20, np.inf, -np.inf, 22], 
		'Marks': [90, 84, 33, 87, 82]} 

df = pd.DataFrame(dict) 
df
