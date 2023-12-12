"""
display the result using tkinter
"""

from ukerie_calculator import result_dict
import pyglet

# global
window = pyglet.window.Window(resizable=True)
print("window.width ",window.width)
print("window.height ",window.height)
bgimage_path = "tileImages/mahjongbg.jpg"
bgimage = pyglet.image.load(bgimage_path)
bg_sprite = pyglet.sprite.Sprite(bgimage)
batch = pyglet.graphics.Batch()
imageWidth = 35
imageHeight = 55
img_list = []

text_label = pyglet.text.Label(
    "Tiles to discard:",
    font_name="Times New Roman",
    font_size=18,
    x=50, y=450,
    anchor_x="left", anchor_y="baseline"
)

text_label_2 = pyglet.text.Label(
    "Effective Tiles to get:",
    font_name="Times New Roman",
    font_size=18,
    x=window.width//2, y=450,
    anchor_x="left", anchor_y="baseline"
)

text_label_3 = pyglet.text.Label(
    "Total Number of Effective Tiles:",
    font_name="Times New Roman",
    font_size=18,
    x=50, y=500,
    anchor_x="left", anchor_y="baseline"
)

tiles_name_dict = {1:"1 Man", 2:"2 Man", 3:"3 Man", 4:"4 Man", 5:"5 Man", 6:"6 Man", 7:"7 Man", 8:"8 Man", 9:"9 Man", 
            11:"1 So", 12:"2 So",13:"3 So",14:"4 So",15:"5 So",16:"6 So",17:"7 So",18:"8 So", 19:"9 So", 
            21:"1 Pin", 22:"2 Pin", 23:"3 Pin", 24:"4 Pin", 25:"5 Pin", 26:"6 Pin", 27:"7 Pin", 28:"8 Pin", 29:"9 Pin", 
            31:"Ton", 32:"Nan", 33:"Sha", 34:"Pei", 35:"Chun", 36:"Haku", 37:"Hatsu"}


# find the max value from dict
values_list = []
for item in result_dict.values():
    values_list.append(item["value"])  
max_value = max(values_list)

text_label_4 = pyglet.text.Label(
    f"{max(values_list)}",
    font_name="Times New Roman",
    font_size=18,
    x=400, y=500,
    anchor_x="left", anchor_y="baseline"
)

# Find all keys with the maximum "value"
keys_with_max_value = []
for key, val in result_dict.items():
    if val["value"] == max_value:
        keys_with_max_value.append(key)



def display_max_val_tile_img():
    """ display the discard tiles """
    for idx, key in enumerate(keys_with_max_value):
        img = pyglet.resource.image(f"tileImages/{key}.png")
        img.width = imageWidth # resize the image
        img.height = imageHeight
        img_x = window.width//10 + img.width
        img_y = window.height//2 - idx * img.height
        sprite = pyglet.sprite.Sprite(img = img, x = img_x, y = img_y, batch = batch)
        img_list.append(sprite)


def display_tile():
    """display effective tiles' image """
    # tile_dict = {}
    tile_img_list = []
    for i in range(len(keys_with_max_value)):
        tile_img_list.append(result_dict[keys_with_max_value[i]]["tiles"])

    for i in range(len(tile_img_list)):
        for idx, num in enumerate(tile_img_list[i]):
            tile_img = pyglet.resource.image(f"tileImages/{num}.png")
            tile_img.width = imageWidth
            tile_img.height = imageHeight
            tile_x = window.width//2 + idx * tile_img.width
            tile_y = window.height//2 - i * tile_img.height
            print("X", tile_x)
            print("Y", tile_y)
            tile_sprite = pyglet.sprite.Sprite(img = tile_img, x = tile_x, y = tile_y, batch = batch)
            img_list.append(tile_sprite)



@window.event
def on_draw():
    window.clear()
    bg_sprite.draw()
    text_label.draw()
    text_label_2.draw()
    text_label_3.draw()
    text_label_4.draw()
    for sprite in img_list:
        sprite.draw()
    

display_max_val_tile_img()
display_tile()
pyglet.app.run()