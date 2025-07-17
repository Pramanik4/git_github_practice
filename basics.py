#!/usr/bin/env python3
print("Bliss")


# ML to start 
import pandas as pd

def data_load_first():
  data = pd.read_csv("/home/pooja/Downloads/Salary Data.csv")
  return data.head()

def data_load_last():
  data = pd.read_csv("/home/pooja/Downloads/Salary Data.csv")
  return data.tail()

data = data_load_first()
data1 = data_load_last()
print(data)
print(data1)