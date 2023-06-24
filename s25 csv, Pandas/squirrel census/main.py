# My solution:
# import pandas

# data = pandas.read_csv('Squirrel_Data.csv')

# colors_list = data['Primary Fur Color'].to_list()

# gray_count = 0
# cinnamon_count = 0
# black_count = 0

# for item in colors_list:
#     if item == 'Gray':
#         gray_count += 1
#     elif item == 'Cinnamon':
#         cinnamon_count += 1
#     elif item == 'Black':
#         black_count += 1

# print(f'Gray: {gray_count} Cinnamon: {cinnamon_count} Black: {black_count}')

# counts_dict = {
#     "colors": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_count, cinnamon_count, black_count]
# }

# print(counts_dict)

# counts_data = pandas.DataFrame(counts_dict)
# print(counts_data)
# counts_data.to_csv('squirrel_counts_data.csv')


# Angela's solution:
import pandas

data = pandas.read_csv('Squirrel_Data.csv')
grey_squirrels = data[data['Primary Fur Color'] == 'Gray']
grey_squirrels_count = len(grey_squirrels)
print(grey_squirrels_count)

red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
red_squirrels_count = len(red_squirrels)
print(red_squirrels_count)

black_squirrels = data[data['Primary Fur Color'] == 'Black']
black_squirrels_count = len(black_squirrels)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_solution_angela.csv')