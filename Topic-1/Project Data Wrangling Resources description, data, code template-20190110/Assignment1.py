# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:18:45 2019

@author: harsh
"""

import pandas as pd
import re
import glob
import copy
import numpy as np

k = glob.glob("data_raw/*")
import matplotlib.pyplot as plt


def Q1_function():
    
    return glob.glob("data_raw/*")
    
    """
    :type : None
    :rtype: List[String]
    """
    # TYPE YOUR CODE HERE
    


# Call the function and print the result. This result is used in subsequent questions.
filenames = Q1_function()
print(filenames)

def Q2_function(files, s):
    for filename in files:
        if re.search(s,filename):
            return filename
            
    """
    :type : List[String], String
    :rtype: String
    """
    # TYPE YOUR CODE HERE
        

# Call the function and print the result. Use this to check the correctness of your code and for debugging.
file = Q2_function(filenames, s = "Dictionaries")
print(file)

def Q3_function(files, s):
    
    return pd.read_excel(Q2_function(files,s))
    
    """
    :type : List[String], String
    :rtype: Pandas DataFrame
    """
    # TYPE YOUR CODE HERE
    

# Call the function and print the result. This result is used in subsequent questions.
functions_df = Q3_function(filenames, s = "Functions")
print(functions_df)
functions_df.head(3)


def Q4_function(dataframe):
    
    dataFrame = dataframe.loc[:,["id", "Time taken", "Grade/45.00", "Q. 1 /5.00", "Q. 2 /10.00", "Q. 3 /6.00", "Q. 4 /6.00", "Q. 5 /12.00", "Q. 6 /6.00"]]
        
    return functions_df.columns,dataframe, functions_df.head(10)
    """
    :type : DataFrame
    :rtype: [String], DataFrame, DataFrame
    """
    # TYPE YOUR CODE HERE
    
# Call the function and print the results. These results are used in subsequent questions.
names, df_subset, top_10 = Q4_function(functions_df)

print("Column Names")
print(names)
print()
print("Subsetted Data")
print(df_subset)
print()
print("Top 10 Rows")
print(top_10)



def changeTimeFormate(timeStr):
    timeInt = 0
    matObj = re.search(r'(\d+) ([m][i][n][s])',timeStr)
    if matObj:
        if len(matObj.groups()) > 1:
            timeInt = int(matObj.group(1)) * 60
        
    matObj = re.search(r'(\d+) ([s][e][c][s])',timeStr)
    if matObj:
        if len(matObj.groups()) > 1:
            timeInt = timeInt + int(matObj.group(1)) 

    return timeInt

def Q5_function(df):
    columnDataTypes = df.dtypes
    newCols = []
    
    print(type(df))
          
    for i in df.columns:
        newCols.append(re.sub(" ","",i))
    print(newCols)
    df.columns = newCols
 
    if not df['Timetaken'].isnull().any():
        df['Timetaken'].fillna(0)

    df['time'] = df['Timetaken'].apply(changeTimeFormate)
    df.drop(columns = ['Timetaken'],axis = 1)
    df = df.drop(['Timetaken'], axis=1)
   
    print(type(df))
    """
    :type : DataFrame
    :rtype: [String], DataFrame
    """
    # TYPE YOUR CODE HERE
    return columnDataTypes, df


# Call the function and print the results. These results are used in subsequent questions.
column_types, Q5_df = Q5_function(df_subset)
print("Column Datatypes")
print(column_types)
print("New Update DataFrame")
print(Q5_df)






def Q6_function(df):
    columnNames = Q5_df.columns.tolist()



    for col in columnNames:
        print(col)
        try:
            if any(df[col] == '-'):
                df[col].replace({'-':np.nan},inplace = True)
                # drop df.col = drop
                df[col]  = df[col].astype(float)
                mean = df[col].astype(float).mean()
                df[col].replace({np.nan:float(mean)},inplace = True)
        except:
            print('exception ',col)
        
    
    dfNew = []
    ### Adding columns 
    for col in columnNames:
        try:
            if col == 'id':
                dfNew.append(-1)
            else:
                dfNew.append(df[col].mean())
        except:
            dfNew.append("NA")
    print(columnNames)
    print(dfNew)
          
    df1  = pd.DataFrame(data = [dfNew], columns= list(columnNames))
    print('##############################3333333')
    print(df1.columns)
    print('##################################3')
    print(df.columns)
    print(df.shape)
    df = df.append(df1)
    print(df.shape)
    print(df.tail())
    return df
    """
    :type : DataFrame
    :rtype: DataFrame
    """
    # TYPE YOUR CODE HERE



# Call the function and print the results.
Q6_df = Q6_function(Q5_df)
print(Q6_df)