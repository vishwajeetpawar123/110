import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def rosm(counter):
    dataset=[]
    for i in range(counter):
        random_i=random.randint(0,len(data)-1)
        value=data[random_i]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


def setup():
    mean_list=[]
    for i in range (0,1000):
        set_om=random_set_of_mean=(100)
        mean_list.append(set_om)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()


#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

