# Reading CSV Data in Python


# Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


# Using csv library
import csv

with open("100 Days of Code\Day 25\Weather\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)


# Using the pandas library
import pandas

data = pandas.read_csv("100 Days of Code\Day 25\Weather\weather_data.csv")

# DataFrame and Series
print(type(data))
print(type(data["temp"]))

# Serialization / IO / conversion
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

# Computations / descriptive stats
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# Get Row data value
monday =data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch and save to csv
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": (76, 56, 65)
}
data = pandas. DataFrame(data_dict)
data.to_csv(r"100 Days of Code\Day 25\Weather\new_data.csv")