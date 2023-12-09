global completeSets
global pair
global partialSets
global bestShanten
global minimumShanten
global hasGivenMinimum

def calculateChiitoitsuShanten(handToCheck):
    # Calculates how many tiles away from chiitoitsu/seven pairs the hand is
    pairCount = 0
    uniqueTiles = 0

    for i in range(1, len(handToCheck)):
        if handToCheck[i] == 0:
            continue

        uniqueTiles += 1

        if handToCheck[i] >=2 :
            pairCount += 1

    shanten = 6 - pairCount
    if uniqueTiles < 7:
        shanten = shanten + 7 - uniqueTiles
    return shanten

def calculateKokushiShanten(handToCheck):
    # Calculates how many tiles away from kokushi/thirteen orphans the hand is
    uniqueTiles = 0
    hasPair = 0
    
    for i in range(1, len(handToCheck)):
        if i % 10 == 1 or i % 10 == 9 or i > 30:
            if handToCheck[i] != 0:
                uniqueTiles += 1

                if handToCheck[i] >= 2:
                    hasPair = 1
    
    return 13 - uniqueTiles - hasPair

def calculateStandardShanten(handToCheck, minimumShanten_ = -2):
    # Calculates how many tiles away from a complete standard hand the given hand is
    
    global hasGivenMinimum
    hasGivenMinimum = True

    global minimumShanten
    minimumShanten = minimumShanten_

    global completeSets
    completeSets = 0

    global pair
    pair = 0

    global partialSets
    partialSets = 0

    global bestShanten
    bestShanten = 8

    def removePotentialSets(i):
        global completeSets
        global pair
        global partialSets
        global bestShanten
        global minimumShanten
        global hasGivenMinimum
        
        if bestShanten <= minimumShanten:
            return
        
        # Skip to the next tile that exists in the hand
        while i < len(handToCheck) and handToCheck[i] == 0:
            i += 1

        # We've checked everything. See if this shanten is better than the current best
        if i >= len(handToCheck):
            bestShanten = min(bestShanten, 8 - (completeSets * 2) - partialSets - pair)
            return
        
        if completeSets + partialSets < 4:
            if handToCheck[i] == 2:
                partialSets += 1
                handToCheck[i] -= 2
                removePotentialSets(i)
                handToCheck[i] += 2
                partialSets -= 1

            if i < 30 and handToCheck[i + 1] != 0:
                partialSets += 1
                handToCheck[i] -= 1
                handToCheck[i + 1] -= 1
                removePotentialSets(i)
                handToCheck[i] += 1
                handToCheck[i + 1] += 1
                partialSets -= 1

            if i < 30 and i % 10 <= 8 and handToCheck[i + 2] != 0:
                partialSets += 1
                handToCheck[i] -= 1
                handToCheck[i + 2] -= 1
                removePotentialSets(i)
                handToCheck[i] += 1
                handToCheck[i + 2] += 1
                partialSets -= 1

        removePotentialSets(i + 1)

    def removeCompletedSets(i):
        # Removes all possible combinations of complete sets from the hand and recursively checks the shanten of each
        global completeSets
        global pair
        global partialSets
        global bestShanten
        global minimumShanten
        global hasGivenMinimum

        if bestShanten <= minimumShanten:
            return

        # Skip to the next tile that exists in the hand
        while i < len(handToCheck) and handToCheck[i] == 0:
            i += 1

        # We've gone through the whole hand, now check for partial sets
        if i >= len(handToCheck):
            removePotentialSets(1)
            return
        
        # Check Triplet
        if handToCheck[i] >= 3:
            completeSets += 1
            handToCheck[i] -= 3
            removeCompletedSets(i)
            handToCheck[i] += 3
            completeSets -= 1
        
        # Check Sequence
        if i < 30 and handToCheck[i + 1] != 0 and handToCheck[i + 2] != 0:
            completeSets += 1
            handToCheck[i] -= 1
            handToCheck[i + 1] -= 1
            handToCheck[i + 2] -= 1
            removeCompletedSets(i)
            handToCheck[i] += 1
            handToCheck[i + 1] += 1
            handToCheck[i + 2] += 1
            completeSets -= 1

        removeCompletedSets(i + 1)
        
    if minimumShanten_ == -2:
        hasGivenMinimum = False
        minimumShanten = -1
    
    for i in range(1, len(handToCheck)):
        if handToCheck[i] >=2:
            pair += 1
            handToCheck[i] -= 2
            removeCompletedSets(1)
            handToCheck[i] += 2
            pair -= 1
    
    removeCompletedSets(1)

    return bestShanten

def calculateMinimumShanten(handToCheck, minimumShanten = -2):
    chiitoiShanten = calculateChiitoitsuShanten(handToCheck)

    # If it's complete with chiitoi, no need to keep checking.
    if chiitoiShanten < 0:
        return chiitoiShanten
    
    '''
    If a hand has a kokushi shanten of 3 or less, it cannot possibly be closer to a standard hand
    Example: 1239m1239s199p123z is 3-shanten for both kokushi and a standard hand
    But 1239m1239s199p112z is 4-shanten for kokushi and 2-shanten for standard
    '''
    kokushiShanten = calculateKokushiShanten(handToCheck)

    if kokushiShanten < 3:
        return kokushiShanten
    
    standardShanten = calculateStandardShanten(handToCheck, minimumShanten)

    return min(standardShanten, chiitoiShanten, kokushiShanten)
    
print(calculateStandardShanten([0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 
                                0, 1, 0, 2, 1, 1, 0, 1, 0, 2,
                                0, 0, 0, 0, 0, 0, 0, 2, 0, 2,
                                0, 0, 0, 0, 0, 0, 0, 0]))