import math
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import decimal

data_csv = pd.read_csv("data.csv")
df_data = pd.DataFrame(data_csv)

load_list = []
date_list = []

for i, row in df_data.iterrows():
    date = row["Date"]
    time = row["Time"]

    date_list.append(time)

    baseline = row["Baseline"]

    load_list.append(baseline)


def do_math(load_list, day_list):
    load_degradation_range = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    temp_list_high = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temp_list_low = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    combined_list = []

    plus_1 = 1
    minus_1 = -1
    for load in load_list:
        x = load + (load * (.04 * plus_1))
        y = load + (load * (.04 * minus_1))

        combined_list.append([x, load, y])

    return combined_list


model = do_math(load_list)

plt.plot(model)
plt.ylabel("Load")
plt.xlabel("Time")
plt.show()