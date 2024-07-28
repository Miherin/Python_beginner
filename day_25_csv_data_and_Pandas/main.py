## Didatically getting the values from the CSV file.
with open("weather_data.csv") as file:
    weather_data = file.readlines()
    print(weather_data)

# Looping through values as Pro.
data = []
for line in open("weather_data.csv"):
    data.append(line.strip(",\n"))
print(data)

## Using in-built function to open the CSV file.
import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
    # temperatures.remove('temp')
    # int_temp = [int(num) for num in temperatures]                   
    # print(int_temp)

## Working with Pandas to read tabular data.
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

temp_list = data["temp"].to_list() # Creates a list of temperature values but the header.
print(round(sum(temp_list)/len(temp_list))) # Average normal coding
print(data["temp"].mean()) # Pandas mean function
print(data["temp"].max()) # Pandas max function

## Get data in the row.
print(data[data.temp == data["temp"].max()]) # Seeks the max temp.
monday = data[data.day == "Monday"] # Getting hold of Monday's line.
print(monday.temp * 9/5 + 32) # Converting to Fahrenheit

## Create a dataframe from coding.
data_dict = {
    "students": ["Bobby", "Fofao", "Lessy"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict) # Use DataFrame to convert dict to tabular
data.to_csv("new_data.csv") # Creates a CSV file from dict values.

## Challenge - Central Park Squirrel Data Analysis
csv_path = "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
data = pandas.read_csv(csv_path)
fur_column = data["Primary Fur Color"]
counts = {"Gray": 0, "Cinnamon": 0, "Black": 0}
for n in fur_column:
    if n == "Gray":
        counts["Gray"] += 1
    if n == "Cinnamon":
        counts["Cinnamon"] += 1
    if n == "Black":  
        counts["Black"] += 1
df = pandas.DataFrame(list(counts.items()), columns=["Color", "Count"])
df.to_csv("new_data.csv")