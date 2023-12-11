"""
display the result using tkinter
"""

import tkinter as tk
from ukerie_calculator import result_dict
from PIL import ImageTk, Image

import matplotlib.pyplot as plt
import numpy as np

# root = tk.Tk()
# root.title("image display")
# frame = tk.Frame(root)
# frame.grid()
# root.geometry('800x600')

tile_dic = {1:"1 Man", 2:"2 Man", 3:"3 Man", 4:"4 Man", 5:"5 Man", 6:"6 Man", 7:"7 Man", 8:"8 Man", 9:"9 Man", 11:"1 So", 12:"2 So",13:"3 So",14:"4 So",15:"5 So",16:"6 So",17:"7 So",18:"8 So", 19:"9 So", 21:"1 Pin", 22:"2 Pin", 23:"3 Pin", 24:"4 Pin", 25:"5 Pin", 26:"6 Pin", 27:"7 Pin", 28:"8 Pin", 29:"9 Pin", 31:"Ton", 32:"Nan", 33:"Sha", 34:"Pei", 35:"Chun", 36:"Haku", 37:"Hatsu"}

values_list = []
for item in result_dict.values():
    values_list.append(item['value'])  

max_value = max(values_list) 

# Find all keys with the maximum 'value'
keys_with_max_value = []
for key, val in result_dict.items():
    if val["value"] == max_value:
        keys_with_max_value.append(key)

# # Retrieve the corresponding data for the keys with the maximum 'value'
# result = {}
# for key in keys_with_max_value:
#     result[key] = result_dict[key]


# imgs_list = []
# for idx, key in enumerate(keys_with_max_value):
#     imgs_list.append(ImageTk.PhotoImage(Image.open(f"/Users/jowb/Documents/neu/fall23/CS5002-Final-Project/tileImages/{key}.png")))
#     tk.Label(root, text=f"Discard: {tile_dic[key]} ",image = imgs_list[idx], compound="bottom").grid(padx=10, pady=10)

# root.mainloop()



for i, key in enumerate(keys_with_max_value):
    if keys_with_max_value:
            max_value_key = keys_with_max_value[0]  # Consider the first key with the largest value
            tiles_list = result_dict[max_value_key]['tiles']
            print(tiles_list)
    path = f"/Users/jowb/Documents/neu/fall23/CS5002-Final-Project/tileImages/{key}.png"
    img = plt.imread(path)
    row = len(keys_with_max_value)
    col = len(tiles_list)
    # print(img)
    plt.subplot(row , col + 1, i * (col + 1) + 1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

    for idx, img_idx in enumerate(tiles_list):
        path = f"/Users/jowb/Documents/neu/fall23/CS5002-Final-Project/tileImages/{img_idx}.png"
        img = plt.imread(path)
        print("path",path)
        plt.subplot(row + 2, col + 2, i * (col + 1) + idx + 1) 
        print(f"row: {row}, Col: {col}", )

        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])


plt.show()
