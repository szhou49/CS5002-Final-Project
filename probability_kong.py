import configuration

kongCount = 0
kong_index = []
remaining_kong_tile_number = []


def find_kongs(hand_to_check):
    global kongCount
    for i in range(1, len(hand_to_check)):
        if hand_to_check[i] == 3:
            kongCount += 1
            kong_index.append(i)
            print(kong_index)


def get_remaining_kong_tile():
    global kong_index, kongCount, remaining_kong_tile_number
    if len(kong_index) == 0:
        return 0
    else:
        for i in range(len(kong_index)):
            remaining_kong_tile_number.append(configuration.remainingTiles[kong_index[i]])


def odd_kong():
    odd_kong = sum(remaining_kong_tile_number) / sum(configuration.remainingTiles)
    formatted_percentage = "{:.10f}%".format(odd_kong*100)
    return formatted_percentage

