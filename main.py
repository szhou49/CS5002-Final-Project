import input_validation
import shanten_calculator
import ukerie_calculator
import output_visuals
import configuration


hand_to_check = configuration.hand_to_check
tiles_on_table = configuration.tiles_on_table

all_tiles = []
for i in range(38):
    all_tiles.append(4)

all_tiles[0] = 0
all_tiles[10] = 0
all_tiles[20] = 0
all_tiles[30] = 0


remainingTiles = [x - y - w for x, y, w in zip(all_tiles, hand_to_check, tiles_on_table)]

# value and tiles dictionary
value_tiles_dic = configuration.value_tiles_dic

# print the dictionary out
for i in range(1, len(value_tiles_dic)):
    print(i, value_tiles_dic[i])



# shanten calculation result
minimun_shanten = shanten_calculator.calculateMinimumShanten(hand_to_check)

output_visuals.get_values(value_tiles_dic)
