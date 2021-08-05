# Creating and testing a card duplicate removal function before adding to cards.py

x = [[2, 'H'],[3, 'H'],[4, 'H'],[5, 'H'],[3, 'H'], [4, 'H'],[4, 'H'],[69, 'H'] ,[5, 'H'],[11, 'H'], [10, 'H'], [11, 'H'], [12, 'H'], [5, 'H'],[11, 'H'],[3, 'H'], [4, 'H'], [6, 'H'],[6, 'H'],[1, 'H'],[2, 'H'],[3, 'H'],[4, 'H'],[5, 'H'],[6, 'H'], [7, 'H'], [8, 'H'], [13, 'H'], [14, 'H'], [2, 'H'], [3, 'H'], [4, 'H'], [5, 'H'], [6, 'H'], [7, 'H'], [8, 'H'], [9, 'H'], [10, 'H'], [11, 'H'],[3, 'H'], [4, 'H'], [5, 'H'], [12, 'H'], [13, 'H'], [14, 'H']]

def remove_duplicates(H):
    h = H[:]
    # clean up by marking duplicates as []
    for i in range(len(h)):
        for j in range(i+1,len(h)):
            if h[i] == h[j] and h[i] != 0:
                h[j] = []
    h.sort() # all [] to front
    done = False
    while not done:
        if h[0] == []:    
            h.pop(0)
        else:
            done = True
    return h

x = remove_duplicates(x)
print(x)
