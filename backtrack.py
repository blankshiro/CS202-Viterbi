#let 0 to be index for H and 1 index for L

# table = [[-2.73,-5.47,-8.21,-11.53,-14.01,-25.65], [-3.32,-6.06,-8.79,-10.94,-14.01,-24.49]]
table = [[-2.74, -5.48, -8.22, -11.54, -14.02, -17.34, -19.55, -22.87, -25.66], [-3.32, -6.06, -8.8, -10.96, -14.02, -16.49, -19.55, -22.02, -24.49]]
state = {0: "H", 1: "L"}


sequence_s = []

for i in range(0, len(table[0])):
    cols = [row[i] for row in table]
    getState = cols.index(max(cols))
    sequence_s.append(state[getState])
    
print(sequence_s)



# def backTracker(table):
    
#     last_row = len(table) - 1
   
#     last_col = len(table[0])
    
#     # max_prob = table[0][0]

#     sequence = []
#     # total = max_prob
#     for i in range(0, last_col):
#         if table[0][i] < table[1][i]:
#             sequence.append("L")
#         else:
#             sequence.append("H")
#     print(sequence)


# backTracker(table)