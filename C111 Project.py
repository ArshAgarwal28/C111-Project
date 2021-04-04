import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

file_data = pd.read_csv("data.csv")
file_data = file_data["reading_time"].tolist()

population_mean = statistics.mean(file_data)
population_stdev = statistics.stdev(file_data)


def random_mean(counter):
    dataset = []
    for count in range(0, counter):
        random_index = random.choice(file_data)
        dataset.append(random_index)

    mean = statistics.mean(dataset)
    return mean


mean_list = []

for i in range(0, 1000):
    set_of_means = random_mean(100)
    mean_list.append(set_of_means)

std1 = statistics.stdev(mean_list)
mean1 = statistics.mean(mean_list)

first_stdev_start, first_stdev_end = mean1 - std1, mean1 + std1
second_stdev_start, second_stdev_end = mean1 - (std1 * 2), mean1 + (std1 * 2)
third_stdev_start, third_stdev_end = mean1 - (std1 * 3), mean1 + (std1 * 3)

fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[third_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="Standard Deviation 3 Start"))
fig.add_trace(go.Scatter(x=[third_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="Standard Deviation 3 End"))

fig.show()

