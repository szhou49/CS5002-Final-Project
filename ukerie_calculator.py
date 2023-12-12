from shanten_calculator import calculateMinimumShanten

def calculateUkeire(hand, remainingTiles, baseShanten = -2):
    # Calculates the ukeire of a hand

    if baseShanten == -2:
        baseShanten = calculateMinimumShanten(hand)

    value = 0
    tiles = []

    for i in range(1, len(hand)):
        if remainingTiles[i] == 0 or remainingTiles[i] % 10 == 0:
            continue

        hand[i] += 1
        if calculateMinimumShanten(hand, baseShanten - 1) < baseShanten:
            value += remainingTiles[i]
            tiles.append(i)
        hand[i] -= 1

    return {"value": value, "tiles": tiles}

def calculateDiscardUkeire(hand, remainingTiles, baseShanten = -2):
    # Calculates the resulting ukeire from each possible discard in the hand
    results = [0 for i in range(len(hand))]

    if baseShanten == -2:
        baseShanten = calculateMinimumShanten(hand)

    # Check the ukeire of each hand that results from each discard
    for i in range(1, len(hand)):
        if hand[i] == 0:
            results[i] = { "value": 0, "tiles": [] }
        
        else:
            hand[i] -= 1
            ukeire = calculateUkeire(hand, remainingTiles, baseShanten)
            hand[i] += 1
            results[i] = ukeire
    
    return results
