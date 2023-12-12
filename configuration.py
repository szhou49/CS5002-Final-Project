import input_validation
import ukerie_calculator
import shanten_calculator
import probability_pon
import probability_kong

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


probability_pon.find_pairs(hand_to_check)
probability_pon.get_remaining_pair_tile()
odd_pon = probability_pon.odd_pon()


probability_kong.find_kongs(hand_to_check)
probability_kong.get_remaining_kong_tile()
odd_kong = probability_kong.odd_kong()
