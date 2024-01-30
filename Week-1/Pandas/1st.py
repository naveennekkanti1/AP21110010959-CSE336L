import pandas as pd 
s = pd.Series([[2, 4, 6, 8], 
               [1, 3, 5, 7], 
               [2, 3, 5, 7]]) 
print("Printing the Original Series of list") 
print(s) 
s = s.apply(pd.Series).stack().reset_index(drop = True) 
  
print("\nPrinting the converted series") 
print(s) 