import input_validation
import ukerie_calculator
import shanten_calculator

hand_to_check = input_validation.hand_to_check
tiles_on_table = input_validation.tiles_on_table


all_tiles = []
for i in range(38):
    all_tiles.append(4)

all_tiles[0] = 0
all_tiles[10] = 0
all_tiles[20] = 0
all_tiles[30] = 0


remainingTiles = [x - y - w for x, y, w in zip(all_tiles, hand_to_check, tiles_on_table)]

value_tiles_dic = ukerie_calculator.calculateDiscardUkeire(hand_to_check, remainingTiles)

minimun_shanten = shanten_calculator.calculateMinimumShanten(hand_to_check)