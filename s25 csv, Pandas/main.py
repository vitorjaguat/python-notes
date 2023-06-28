

# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open('weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != 'temp':
#             temperatures.append(int(temp))
#     print(temperatures)       

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# print(data.to_dict())
temp_list = data['temp'].to_list()
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp

# temp_sum = sum(temp_list)
# avarage_temp = temp_sum / len(temp_list)
# print(avarage_temp)

# print(data['temp'].mean())
# print(data['temp'].max())

# return only the Monday row:
# print(data[data.day == 'Monday'])

# return the row with the maximun temperature:
# print(data[data.temp == data.temp.max()])

# return the temperature of Monday in Fahrenheit:
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp)
# monday_temp_fahrenheit = (monday_temp * 9/5) + 32
# print(monday_temp_fahrenheit)

# create a Dataframe from scratch:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
# storing as a .csv file:
data.to_csv('new_data.csv')