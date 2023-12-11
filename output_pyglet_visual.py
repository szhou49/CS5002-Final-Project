"""
display the result using tkinter
"""

from ukerie_calculator import result_dict
import pyglet
from pyglet import image

# global
window = pyglet.window.Window(resizable=True)
batch = pyglet.graphics.Batch()
imageWidth = 50
imageHeight = 75
tile_dic = {1:"1 Man", 2:"2 Man", 3:"3 Man", 4:"4 Man", 5:"5 Man", 6:"6 Man", 7:"7 Man", 8:"8 Man", 9:"9 Man", 
            11:"1 So", 12:"2 So",13:"3 So",14:"4 So",15:"5 So",16:"6 So",17:"7 So",18:"8 So", 19:"9 So", 
            21:"1 Pin", 22:"2 Pin", 23:"3 Pin", 24:"4 Pin", 25:"5 Pin", 26:"6 Pin", 27:"7 Pin", 28:"8 Pin", 29:"9 Pin", 
            31:"Ton", 32:"Nan", 33:"Sha", 34:"Pei", 35:"Chun", 36:"Haku", 37:"Hatsu"}


values_list = []
for item in result_dict.values():
    values_list.append(item['value'])  

max_value = max(values_list) 

# Find all keys with the maximum 'value'
keys_with_max_value = []
for key, val in result_dict.items():
    if val["value"] == max_value:
        keys_with_max_value.append(key)


img_list = []
def display_img():
    xd = 0
    yd = 0
    for idx, key in enumerate(keys_with_max_value):
        img = pyglet.resource.image(f"tileImages/{key}.png")
        img.width = imageWidth
        img.height = imageHeight
        sprite = pyglet.sprite.Sprite(img = img, x = xd, y = window.height//3 + img.height * idx, batch = batch)
        img_list.append(sprite)
        # label_x = xd + img.width + 10  # Adjust label position relative to the image sprite
        # label_y = window.height // 3 + img.height * idx + img.height // 2  # Center label vertically
        # label = pyglet.text.Label(f" ##### {tile_dic[key]}", font_name='Times New Roman', font_size=30, color=(255, 250, 250, 255), x=0, y=0,batch=batch)
        # img_list.append(label)

def display_tile():
        if keys_with_max_value:
            max_value_key = keys_with_max_value[0]
            tiles_list = result_dict[max_value_key]['tiles']
            print("@@@",tiles_list)

        for idx, key in enumerate(tiles_list):
            tile_img = pyglet.resource.image(f"tileImages/{key}.png")
            tile_img.width = imageWidth
            tile_img.height = imageHeight
            largest_value_img = pyglet.resource.image(f"tileImages/{max_value_key}.png")
            largest_value_img.width = imageWidth
            largest_value_img.height = imageHeight
            # tile_sprite = pyglet.sprite.Sprite(img = tile_img, x = tile_img.width + (idx * tile_img.width), y= tile_img.height, batch = batch)
            tile_sprite = pyglet.sprite.Sprite(img=tile_img, x= idx * tile_img.width + tile_img.width, y=window.height//3 + tile_img.height, batch=batch)
            img_list.append(tile_sprite)
            # img_list.append(tile_sprite)


@window.event
def on_draw():
    window.clear()
    for sprite in img_list:
        sprite.draw()
    

display_img()
display_tile()
pyglet.app.run()