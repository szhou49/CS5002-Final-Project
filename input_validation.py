import re


def get_handcards(string):
    """ Check if the input is valid and read the contents of the hand.
    If the input is invalid, output an error message and return None.
    """

    fullmatch = re.fullmatch(r'(\d+[mps]|[1-7]+z)+', string)
    if not fullmatch:
        print("Invalid input!")
        return None

    match = re.findall(r'\d+[mps]|[1-7]+z', string)
    carddict = {
        'm': [], 'p': [], 's': [], 'z': []
    }

    for cards in match:
        type_ = cards[-1]
        for i in cards[:-1]:
            carddict[type_].append(int(i))
        carddict[type_].sort()
    num = sum(len(carddict[tp]) for tp in 'mpsz')

    if num != 14:
        print("Invalid number of tiles! Tiles in hand must be 14.")
        return None
    for tp in 'mpsz':
        for i in set(carddict[tp]):
            if carddict[tp].count(i) > 4:
                break
        else:
            continue
        print('Invalid number of tiles! Each type of tile cannot exceed 4.')
        break
    else:
        return carddict
    return None
