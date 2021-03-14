import sys
# state = ["H", "L"]
# observations = ["A", "C", "G", "T"]
# start_prob = [0.5, ]

# note we should log probabilities so it is much easier
# for indexing purpose
state = {0: "H", 1: "L"} 
start_prob = {"H" : -1, "L": -1}

transition_prob = {"H": {"H": -1, "L": -1}, "L": {"H": -1.322, "L": -0.737}}
sequence_prob = {"H": {"A": -2.322, "C": -1.737, "G": -1.737, "T": -2.322},
"L": {"A": -1.737, "C": -2.322, "G": -2.322, "T": -1.737}}

# [0]*number of cols for i in range(row)
# Instead of using hashmap, i use 2d list instead, easier to understand
table = [[0]*9 for i in range(2)]

string = "GGCACTGAA"

#initialize the first column with start prob + sequence prob:
for i in range(0, len(table)):
    state_c = state.get(i)
    table[i][0] = round(start_prob.get(state_c) + sequence_prob[state_c][string[0]], 2)


#note : table[0][1] = -1.737 + max(table[0][0] + transition_prob[state[0]][state[0]], table[1][0] + transition_prob[state[1]][state[0]])
#this above statement is equivalent to -1.737 + max(table[H][col 0] + transition_prob[H][H], table[L][0] + transition_prob[L][H])

for i in range(1, len(table[0])):
    letter = string[i]

    for j in range(0, len(table)):
        ans = -sys.maxsize - 1
        letter_prob = sequence_prob[state[j]][letter]
        for k in range(0, len(table)):
            p_state = transition_prob[state[k]][state[j]]
            ans = max(ans, table[k][i-1] + p_state)

        table[j][i] = round(ans + letter_prob, 2)


print(table)



