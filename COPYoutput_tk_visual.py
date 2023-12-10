"""
display the result using tkinter
"""
from matplotlib import pyplot
import cv2
from PIL import Image
from ukerie_calculator import result_dict


values_list = []
for item in result_dict.values():
    values_list.append(item['value'])  

max_value = max(values_list) 

# Find all keys with the maximum 'value'
keys_with_max_value = []
for key, val in result_dict.items():
    if val["value"] == max_value:
        keys_with_max_value.append(key)

# Retrieve the corresponding data for the keys with the maximum 'value'
result = {}
for key in keys_with_max_value:
    result[key] = result_dict[key]


fig = pyplot.figure(figsize=(10, 7)) 
num_images = len(keys_with_max_value)
rows = 2
columns = 2
# num_cols = 3  
# num_rows = (num_images + num_cols - 1) // num_cols
fig.add_subplot(rows, columns, 1)


image_list =[]
for i, key in enumerate(keys_with_max_value):
    image_path = cv2.imread(f"/Users/jowb/Documents/neu/fall23/CS5002-Final-Project/tileImages/{key}.png")
    image_list.append(image_path)
    fig.add_subplot(rows, columns, i)



pyplot.tight_layout()
pyplot.show()