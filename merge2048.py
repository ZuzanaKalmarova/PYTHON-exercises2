"""
Merge function for 2048 game.
"""

def move_tiles(worklist):
    """
    Function that slides tiles to next available position
    """
    slidelist = []
    for index in range(len(worklist)):
        if worklist[index] != 0:
            slidelist.append(worklist[index])
    zerolist = [0] * (len(worklist)-len(slidelist))
    slidelist.extend(zerolist)                                
    return slidelist

def join_tiles(worklist, index):
    """
    Function that merges two tiles with same value 
    next to each other to form one tile with double value
    """
    joinlist = list(worklist)
    if joinlist[index] == joinlist[index+1]:
        joinlist[index] *= 2
        joinlist[index+1] = 0
    return joinlist

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    worklist = list(move_tiles(line))
    #resultlist = [0]* len(worklist)
    for index in range(len(worklist)-1):
        if worklist[index] == 0:
            worklist = move_tiles(worklist)
        worklist = join_tiles(worklist, index) 
    return worklist

#print merge([2,2,4,4])

#print merge([2, 0, 2, 4]), "should return [4, 4, 0, 0]"
#print merge([0, 0, 2, 2]), "should return [4, 0, 0, 0]"
#print merge([2, 2, 0, 0]), "should return [4, 0, 0, 0]"
#print merge([2, 2, 2, 2, 2]), "should return [4, 4, 2, 0, 0]"
#print merge([8, 16, 16, 8]), "should return [8, 32, 8, 0]"





