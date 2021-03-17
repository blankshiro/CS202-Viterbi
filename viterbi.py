#!/usr/bin/env python3

# Viterbi Algorithm by CS202 G1T1:
# Cheyenne Jan Lee
# Edwin Tok Wei Liang
# Lee It Tat
# Madeleine Hoo Jia Lei
# Pang Huan Shan, Shawn
# Tan Jun An


def print_table(title, table, states, observations):
    """Helper function to pretty print table of probabilities"""
    print(title + ':')
    pretty_table = []
    pretty_table.append([''] + list(observations))
    for i, row in enumerate(table):
        pretty_table.append([states[i]] + row)
    row_format = '{:>1}' + '{:>8}' * (len(pretty_table[0]) - 1)
    print(row_format.format(*pretty_table[0]))
    row_format = '{:>1}' + '{:>8.2f}' * (len(pretty_table[0]) - 1)
    for row in pretty_table[1:]:
        print(row_format.format(*row))
    print()


def get_sequence(table, states):
    """Retrieves the most likely sequence/path of hidden states from the final table of probabilities from Viterbi algorithm"""

    cols = zip(*table) # 'transpose' the table, so we can access by columns
    return [states[col.index(max(col))] for col in cols] # retrieve corresponding state for the max val of each column


def viterbi(states, start_prob, transition_prob, emission_prob, observations):
    """Finds the most likely sequence/path of hidden states that has generated the given observation.
    This is a log-variant of Viterbi, which means it works with log probabilities only. Additions are used instead of
    mulitiplications when dealing with the probabilities, which improves accuracy and improves complexity.
    """

    # Allocate a 2D table to store our final probabilities; size is states x length of observations
    table = [[0] * len(observations) for i in range(len(states))]

    # Initialize the first column with start prob + emission prob for the first observation:
    for row_index, state in enumerate(states):
        table[row_index][0] = start_prob[state] + emission_prob[state][observations[0]]
    print_table('Initialized table with first column filled', table, states, observations)

    # For each observation i, starting from index 1
    for i in range(1, len(observations)):
        observation = observations[i]
        # For each state j
        for j in range(len(states)):
            ans = -float('inf')
            # For each state k (before j, leading to j)
            for k in range(len(states)):
                observation_p = emission_prob[states[j]][observation] # Probability of observation being emitted given state j: P(observation|state j)
                transition_p = transition_prob[states[k]][states[j]] # Probability of transition to state j given state k: P(transition to state j|state k)
                observation_state_p = observation_p + transition_p # Probability of observation and state: P(observation, state j) = P(observation|state j) + P(transition to state j|state k)
                ans = max(ans, table[k][i-1] + observation_state_p)
            table[j][i] = ans
    print_table('Table with final probability values', table, states, observations)

    return get_sequence(table, states)


def main():
    # Note: we use log probabilities for an improved accuracy and improved complexity as we perform additions instead of multiplications

    # Hidden Markov Model
    states = ('H', 'L')
    start_prob = {
        'H': -1, # 50%
        'L': -1  # 50%
    }
    transition_prob = {
        'H': {'H': -1,     'L': -1},
        'L': {'H': -1.322, 'L': -0.737}
    }
    emission_prob = {
        'H': {'A': -2.322, 'C': -1.737, 'G': -1.737, 'T': -2.322},
        'L': {'A': -1.737, 'C': -2.322, 'G': -2.322, 'T': -1.737}
    } # observations include: 'A', 'C', 'G' and 'T'

    # The sequence of observations
    observations = 'GGCACTGAA'

    # Perform Viterbi algorithm
    most_likely_path = viterbi(states, start_prob, transition_prob, emission_prob, observations)
    print(most_likely_path)


if __name__ == '__main__':
    main()