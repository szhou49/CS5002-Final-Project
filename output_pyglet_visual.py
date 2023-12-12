"""
display the result using tkinter
"""

from configuration import value_tiles_dic, minimun_shanten
import pyglet

# global
window = pyglet.window.Window(resizable=True, visible = False)
bgimage_path = "tileImages/mahjongbg.jpg"
bgimage = pyglet.image.load(bgimage_path)
bg_sprite = pyglet.sprite.Sprite(bgimage)
batch = pyglet.graphics.Batch()
imageWidth = 35
imageHeight = 55
img_list = []
result_dict = value_tiles_dic

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

text_label_4 = pyglet.text.Label(
    "Minimum Shanten:",
    font_name="Times New Roman",
    font_size=18,
    x=window.width//2, y=500,
    anchor_x="left", anchor_y="baseline"
)

# find the max value from dict
max_value = 0

for i in range(1, len(result_dict)):
    if result_dict[i]["value"] >= max_value:
        max_value = result_dict[i]["value"]

# Find all keys with the maximum "value"
keys_with_max_value = []
tiles = []
for i in range(1, len(result_dict)):
    if result_dict[i]["value"] == max_value:
        keys_with_max_value.append(i)
        tiles.append(result_dict[i]["tiles"])

text_label_5 = pyglet.text.Label(
    f"{max_value}",
    font_name="Times New Roman",
    font_size=18,
    x=400, y=500,
    anchor_x="left", anchor_y="baseline"
)

text_label_6 = pyglet.text.Label(
    f"{minimun_shanten}",
    font_name="Times New Roman",
    font_size=18,
    x=window.width//2 + 250, y=500,
    anchor_x="left", anchor_y="baseline"
)


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
            tile_sprite = pyglet.sprite.Sprite(img = tile_img, x = tile_x, y = tile_y, batch = batch)
            img_list.append(tile_sprite)

def main():
    @window.event
    def on_draw():
        window.clear()
        bg_sprite.draw()
        text_label.draw()
        text_label_2.draw()
        text_label_3.draw()
        text_label_4.draw()
        text_label_5.draw()
        text_label_6.draw()
        for sprite in img_list:
            sprite.draw()

    display_max_val_tile_img()
    display_tile()
    pyglet.app.run()

