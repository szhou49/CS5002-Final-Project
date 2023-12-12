import configuration

pairCount = 0
pair_index = []
remaining_pair_tile_number = []


def find_pairs(hand_to_check):
    global pairCount
    for i in range(1, len(hand_to_check)):
        if hand_to_check[i] == 2:
            pairCount += 1
            pair_index.append(i)


def get_remaining_pair_tile():
    global pairCount, pair_index, remaining_pair_tile_number
    if len(pair_index) == 0:
        return 0
    else:
        for i in range(len(pair_index)):
            remaining_pair_tile_number.append(configuration.remainingTiles[pair_index[i]])


def odd_pon():
    odd_chow = sum(remaining_pair_tile_number) / sum(configuration.remainingTiles)

    return odd_chow

