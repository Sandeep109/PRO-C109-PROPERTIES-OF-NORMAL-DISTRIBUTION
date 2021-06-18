import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
height = df["math score"].to_list()


mean = sum(height)/len(height)
sd = statistics.stdev(height)
median = statistics.median(height)
mode = statistics.mode(height)

print("mean :-",mean)
print("median :-",median)
print("mode :-",mode)
print("sd :-",sd)

#fig = ff.create_distplot([dice_result], ["result"], show_hist=False)
#fig.show()

first_sd_start,first_sd_end = mean-sd, mean+sd
second_sd_start,second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start,third_sd_end = mean-(3*sd), mean+(3*sd)

data_within_1_sd = [result for result in height if result>first_sd_start and result<first_sd_end]
data_within_2_sd = [result for result in height if result>second_sd_start and result<second_sd_end]
data_within_3_sd = [result for result in height if result>third_sd_start and result<third_sd_end]

print("{}% of data lies within one sd".format(len(data_within_1_sd)*100.0/len(height)))
print("{}% of data lies within two sd".format(len(data_within_2_sd)*100.0/len(height)))
print("{}% of data lies within three sd".format(len(data_within_3_sd)*100.0/len(height)))
